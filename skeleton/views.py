import json
import logging
import datetime
import requests

from django.conf import settings
from django.contrib.auth import logout
from django.shortcuts import redirect, render, Http404
from .models import PublicExperience
from openhumans.models import OpenHumansMember
import io
import uuid

from StepperComponent import Stepper

logger = logging.getLogger(__name__)


def index(request, page="home"):
    """
    Starting page for app.
    """

    context = {
        "navpage": page,
        "navlinks": [
            {
                "linkTitle": "Home",
                "linkLoc": "/home",
                "linkName": "home",
                "template": "home.html"
            },
            {
                "linkTitle": "About",
                "linkLoc": "/about",
                "linkName": "about",
                "template": "about.html"
            },
            {
                "linkTitle": "Share",
                "linkLoc": "/share",
                "linkName": "share",
                "template": "share.html"
            },
            {
                "linkTitle": "Login",
                "linkLoc": "/login",
                "linkName": "login",
                "template": "login.html"
            }
        ],
        "stepper": [
            {
                "id": 1,
                "label": "Login"
            },
            {
                "id": 2,
                "label": "Define Profile"
            },
            {
                "id": 3,
                "label": "Add Event"
            }
        ],
        "ueftext": [
            {
                "rows": [
                    {
                        "qtext": "Where",
                        "qcolour": "#4d75ad",
                        "phtext": "Enter name of location or postcode...",
                        "input": "ip"

                    }
                ],
                "maintext": "Where..."
            },
            {
                "rows": [
                    {
                        "qtext": "What",
                        "qcolour": "#ffbb5d",
                        "phtext": "Your experience can be entered here...",
                        "input": "ta"
                    }
                ],
                "maintext": "Enter your experience"
            },
            {
                "rows": [
                    {
                        "qtext": "What",
                        "qcolour": "#ffbb5d",
                        "phtext": "",
                        "input": "ta"
                    }
                ],
                "maintext": "What would you have wished to be different?"
            }
        ],
        "user_exp": [
            {
                "id": "32097868",
                "datetime": "Sept 18, 2019, 10:31 a.m.",
                "user_txt": [
                    {
                        "question": "Event",
                        "text": "The air conditioning in the room where I was having a meeting was really loud and I found it really hard to concentrate."
                    },
                    {
                        "question": "What would you have liked to be different?",
                        "text": ""
                    }
                ]
            },
            {
                "id": "19279611",
                "datetime": "Sept 17, 2019, 8:46 a.m.",
                "user_txt": [
                    {
                        "question": "Event",
                        "text": "The tube is too loud."
                    },
                    {
                        "question": "What would you have liked to be different?",
                        "text": ""
                    }
                ]
            },
            {
                "id": "32097868",
                "datetime": "Sept 17, 2019, 8:45 a.m.",
                "user_txt": [
                    {
                        "question": "Event",
                        "text": "I'm at a conference today and I found people not using the microphone really difficult - it makes it much harder to concentrate on what they were saying. I was much more distracted."
                    },
                    {
                        "question": "What would you have liked to be different?",
                        "text": ""
                    }
                ]
            }
        ],
        "MONE_data": [
            {
                "UID": "0000001",
                "EID": "32097868",
                "date": "18/09/19",
                "Event_What": "The air conditioning in the room where I was having a meeting was really loud and I found it really heard to concentrate, it was a rubbish experience.",
                "Location_Where": "NW1 2HS",
                "LikeToBeDifferent": "I would have liked the air conditioning to less loud to aid my concentration",
                "Summary": "Loud Air Conditioning"
            },
            {
                "UID": "0000002",
                "EID": "32097867",
                "date": "17/09/19",
                "Event_What": "The tube is too loud.",
                "Location_Where": "NW1 8NH",
                "LikeToBeDifferent": "would have liked the tube to be less loud",
                "Summary": "Loud Tube"
            },
            {
                "UID": "0000003",
                "EID": "32097866",
                "date": "17/09/19",
                "Event_What": "I'm at a conference today and I found the people not using the microphone really difficult - it makes it harder to concentrate on what they were saying. I was much more distracted.",
                "Location_Where": "SE15 5DQ",
                "LikeToBeDifferent": "For people in conferences to use a microphone. To aid my concentration and reduce my distraction.",
                "Summary": "None use of microphone in conference"
            }
        ],
        "Documentation_data":[
            {
            "ID": "0000001",
            "Date": "14/06/2019",
            "Group": "moderation",
            "Name": "experience-moderation-guidlines",
            "Version": "0.4"
            },
            {
            "ID": "0000002",
            "Date": "02/09/2020",
            "Group": "moderation",
            "Name": "why-is-there-a-moderation-process",
            "Version": "1"
            },
            {
            "ID": "0000003",
            "Date": "09/11/2020",
            "Group": "instructional",
            "Name": "experience-creation-and-submission",
            "Version": "2"
            },
        ],
        "AP_data": [
            {
                "Title": "Navigation Adjustment",
                "ID": "navadjust",
                "arrow": "arrow_expandingpanel_na"
            },
            {
                "Title": "Colour Adjustment",
                "ID": "coladjust",
                "arrow": "arrow_expandingpanel_ca"
            },
            {
                "Title": "Content Adjustment",
                "ID": "contadjust",
                "arrow": "arrow_expandingpanel_cta"
            }
        ],
        "AP_blank":
            {
                "Title": "Expanding Panel",
                "ID": "blankexpanel",
                "arrow": "arrow_expandingpanel_bep",
                "content": "Content that can be replaced"
        },
        'AP_gallery_panels':
            {
                "Title": "Panel Components - These components are based on core Bootstap components and form the core structural elements of the platform.",
                "ID": "gal_expanel_panels",
                "arrow": "arrow_expandingpanel_bep"
        },
        'AP_gallery_animated_panels':
            {
                "Title": "Animated Panel Components - These components are animated using javascript to show and hide them. They are core structural elements of the platform.",
                "ID": "gal_expanel_animated_panel",
                "arrow": "arrow_expandingpanel_bep"
        },
            'AP_gallery_navigation':
            {
                "Title": "Navigation Components - These components are used for platform navigation, they allow the platform user to move around the available sections/pages of the platform and to other related content.",
                "ID": "gal_expanel_navigation",
                "arrow": "arrow_expandingpanel_bep"
        },
        'AP_HCL':
            {
                "Desc": "Some people cannot read text if there is not sufficient contrast between the text and background. For others, bright colours (high luminance) are not readable; they need low luminance."
        },
        "peed_ele_row": [
            {
                "peed_ele_col": [
                    {
                        "text": "I",
                        "icon": "icon-Autistic-Person"
                    },
                    {
                        "text": "Audio Desc",
                        "icon": "icon-audio-description"
                    },
                    {
                        "text": "Account",
                        "icon": "icon-account_circle"
                    },
                    {
                        "text": "Add box",
                        "icon": "icon-add_box"
                    }
                ]
            },
            {
                "peed_ele_col": [
                    {
                        "text": "Add",
                        "icon": "icon-add"
                    },
                    {
                        "text": "Apps",
                        "icon": "icon-apps-24px"
                    },
                    {
                        "text": "Bar Chart",
                        "icon": "icon-bar_chart"
                    },
                    {
                        "text": "Camera",
                        "icon": "icon-camera_alt"
                    }
                ]
            },
            {
                "peed_ele_col": [
                    {
                        "text": "Tick",
                        "icon": "icon-check-circle-together"
                    },
                    {
                        "text": "Cross",
                        "icon": "icon-close"
                    },
                    {
                        "text": "Smile",
                        "icon": "icon-comment-alt-smile"
                    },
                    {
                        "text": "Compass",
                        "icon": "icon-compass"
                    }
                ]
            },
            {
                "peed_ele_col": [
                    {
                        "text": "CSP",
                        "icon": "icon-csp-lblue"
                    },
                    {
                        "text": "Database",
                        "icon": "icon-database-solid"
                    },
                    {
                        "text": "Email",
                        "icon": "icon-email"
                    },
                    {
                        "text": "Fast Food",
                        "icon": "icon-fastfood"
                    }
                ]
            },
            {
                "peed_ele_col": [
                    {
                        "text": "Image",
                        "icon": "icon-image"
                    },
                    {
                        "text": "School",
                        "icon": "icon-school"
                    },
                    {
                        "text": "Language",
                        "icon": "icon-language"
                    },
                    {
                        "text": "No",
                        "icon": "icon-no"
                    }
                ]
            },
        ],
        "peed_fld": [
            {
                "number": "2.",
                "title": "Sensory"
            }
        ],
        "peed_ele_master": [
            {
                "text": "I",
                        "icon": "icon-Autistic-Person"
            },
            {
                "text": "Audio Desc",
                        "icon": "icon-audio-description"
            },
            {
                "text": "Account",
                        "icon": "icon-account_circle"
            },
            {
                "text": "Add box",
                        "icon": "icon-add_box"
            },
            {
                "text": "Add",
                        "icon": "icon-add"
            },
            {
                "text": "Apps",
                        "icon": "icon-apps-24px"
            },
            {
                "text": "Bar Chart",
                        "icon": "icon-bar_chart"
            },
            {
                "text": "Camera",
                        "icon": "icon-camera_alt"
            },
            {
                "text": "Tick",
                        "icon": "icon-check-circle-together"
            },
            {
                "text": "Cross",
                        "icon": "icon-close"
            },
            {
                "text": "Smile",
                        "icon": "icon-comment-alt-smile"
            },
            {
                "text": "Compass",
                        "icon": "icon-compass"
            },
            {
                "text": "CSP",
                        "icon": "icon-csp-lblue"
            },
            {
                "text": "Database",
                        "icon": "icon-database-solid"
            },
            {
                "text": "Email",
                        "icon": "icon-email"
            },
            {
                "text": "Fast Food",
                        "icon": "icon-fastfood"
            },
            {
                "text": "Image",
                        "icon": "icon-image"
            },
            {
                "text": "School",
                        "icon": "icon-school"
            },
            {
                "text": "Language",
                        "icon": "icon-language"
            },
            {
                "text": "No",
                        "icon": "icon-no"
            }
        ],

    }
    stepper_object = Stepper.Stepper(request)

    stepper_object.update()

    auth_url = OpenHumansMember.get_auth_url()
    context = {**context, **{'auth_url': auth_url}}  # ,
#                             'oh_proj_page': settings.OH_PROJ_PAGE}}
    if request.user.is_authenticated:
        return redirect('overview')
    # return render(request, 'index.html', context=context)

#    if(page == "error"):
#        raise Http404("page does not exist: error")
#    else:
    return render(request, 'index.html', context=context)



def split(request, page="home"):
    """
    Starting page for app.
    """

    context = {
        "navpage": page,
        "navlinks": [
            {
                "linkTitle": "Home",
                "linkLoc": "/split/home",
                "linkName": "home",
                "template": "home.html"
            },
            {
                "linkTitle": "About",
                "linkLoc": "/split/about",
                "linkName": "about",
                "template": "about.html"
            },
            {
                "linkTitle": "Share",
                "linkLoc": "/split/share",
                "linkName": "share",
                "template": "share.html"
            },
            {
                "linkTitle": "Login",
                "linkLoc": "/split/login",
                "linkName": "login",
                "template": "login.html"
            }
        ],
        "stepper": [
            {
                "id": 1,
                "label": "Login"
            },
            {
                "id": 2,
                "label": "Define Profile"
            },
            {
                "id": 3,
                "label": "Add Event"
            }
        ],
        "ueftext": [
            {
                "rows": [
                    {
                        "qtext": "Where",
                        "qcolour": "#4d75ad",
                        "phtext": "Enter name of location or postcode...",
                        "input": "ip"
                    },
                    {
                        "qtext": "What",
                        "qcolour": "#ffbb5d",
                        "phtext": "Your experience can be entered here...",
                        "input": "ta"
                    }
                ],
                "maintext": "Enter your experience"
            },
            {
                "rows": [
                    {
                        "qtext": "What",
                        "qcolour": "#ffbb5d",
                        "phtext": "",
                        "input": "ta"
                    }
                ],
                "maintext": "What would you have wished to be different?"
            }
        ],
        "user_exp": [
            {
                "id": "32097868",
                "datetime": "Sept 18, 2019, 10:31 a.m.",
                "user_txt": [
                    {
                        "question": "Event",
                        "text": "The air conditioning in the room where I was having a meeting was really loud and I found it really hard to concentrate."
                    },
                    {
                        "question": "What would you have liked to be different?",
                        "text": ""
                    }
                ]
            },
            {
                "id": "19279611",
                "datetime": "Sept 17, 2019, 8:46 a.m.",
                "user_txt": [
                    {
                        "question": "Event",
                        "text": "The tube is too loud."
                    },
                    {
                        "question": "What would you have liked to be different?",
                        "text": ""
                    }
                ]
            },
            {
                "id": "32097868",
                "datetime": "Sept 17, 2019, 8:45 a.m.",
                "user_txt": [
                    {
                        "question": "Event",
                        "text": "I'm at a conference today and I found people not using the microphone really difficult - it makes it much harder to concentrate on what they were saying. I was much more distracted."
                    },
                    {
                        "question": "What would you have liked to be different?",
                        "text": ""
                    }
                ]
            }
        ],
        "MONE_data": [
            {
                "UID": "0000001",
                "EID": "32097868",
                "date": "18/09/19",
                "Event_What": "The air conditioning in the room where I was having a meeting was really loud and I found it really heard to concentrate, it was a rubbish experience.",
                "Location_Where": "NW1 2HS",
                "LikeToBeDifferent": "I would have liked the air conditioning to less loud to aid my concentration",
                "Summary": "Loud Air Conditioning"
            },
            {
                "UID": "0000002",
                "EID": "32097867",
                "date": "17/09/19",
                "Event_What": "The tube is too loud.",
                "Location_Where": "NW1 8NH",
                "LikeToBeDifferent": "would have liked the tube to be less loud",
                "Summary": "Loud Tube"
            },
            {
                "UID": "0000003",
                "EID": "32097866",
                "date": "17/09/19",
                "Event_What": "I'm at a conference today and I found the people not using the microphone really difficult - it makes it harder to concentrate on what they were saying. I was much more distracted.",
                "Location_Where": "SE15 5DQ",
                "LikeToBeDifferent": "For people in conferences to use a microphone. To aid my concentration and reduce my distraction.",
                "Summary": "None use of microphone in conference"
            }
        ],
        "Documentation_data":[
            {
            "ID": "0000001",
            "Date": "14/06/2019",
            "Group": "moderation",
            "Name": "experience-moderation-guidlines",
            "Version": "0.4"
            },
            {
            "ID": "0000002",
            "Date": "02/09/2020",
            "Group": "moderation",
            "Name": "why-is-there-a-moderation-process",
            "Version": "1"
            },
            {
            "ID": "0000003",
            "Date": "09/11/2020",
            "Group": "instructional",
            "Name": "experience-creation-and-submission",
            "Version": "2"
            },
        ],
        "AP_data": [
            {
                "Title": "Navigation Adjustment",
                "ID": "navadjust",
                "arrow": "arrow_expandingpanel_na"
            },
            {
                "Title": "Colour Adjustment",
                "ID": "coladjust",
                "arrow": "arrow_expandingpanel_ca"
            },
            {
                "Title": "Content Adjustment",
                "ID": "contadjust",
                "arrow": "arrow_expandingpanel_cta"
            }
        ],
        "AP_blank":
            {
                "Title": "Expanding Panel",
                "ID": "blankexpanel",
                "arrow": "arrow_expandingpanel_bep",
                "content": "Content that can be replaced"
        },
        'AP_gallery_panels':
            {
                "Title": "Panel Components - These components are based on core Bootstap components and form the core structural elements of the platform.",
                "ID": "gal_expanel_panels",
                "arrow": "arrow_expandingpanel_bep"
        },
        'AP_gallery_animated_panels':
            {
                "Title": "Animated Panel Components - These components are animated using javascript to show and hide them. They are core structural elements of the platform.",
                "ID": "gal_expanel_animated_panel",
                "arrow": "arrow_expandingpanel_bep"
        },
            'AP_gallery_navigation':
            {
                "Title": "Navigation Components - These components are used for platform navigation, they allow the platform user to move around the available sections/pages of the platform and to other related content.",
                "ID": "gal_expanel_navigation",
                "arrow": "arrow_expandingpanel_bep"
        },
        'AP_HCL':
            {
                "Desc": "Some people cannot read text if there is not sufficient contrast between the text and background. For others, bright colours (high luminance) are not readable; they need low luminance."
        },
        "peed_ele_row": [
            {
                "peed_ele_col": [
                    {
                        "text": "I",
                        "icon": "icon-Autistic-Person"
                    },
                    {
                        "text": "Audio Desc",
                        "icon": "icon-audio-description"
                    },
                    {
                        "text": "Account",
                        "icon": "icon-account_circle"
                    },
                    {
                        "text": "Add box",
                        "icon": "icon-add_box"
                    }
                ]
            },
            {
                "peed_ele_col": [
                    {
                        "text": "Add",
                        "icon": "icon-add"
                    },
                    {
                        "text": "Apps",
                        "icon": "icon-apps-24px"
                    },
                    {
                        "text": "Bar Chart",
                        "icon": "icon-bar_chart"
                    },
                    {
                        "text": "Camera",
                        "icon": "icon-camera_alt"
                    }
                ]
            },
            {
                "peed_ele_col": [
                    {
                        "text": "Tick",
                        "icon": "icon-check-circle-together"
                    },
                    {
                        "text": "Cross",
                        "icon": "icon-close"
                    },
                    {
                        "text": "Smile",
                        "icon": "icon-comment-alt-smile"
                    },
                    {
                        "text": "Compass",
                        "icon": "icon-compass"
                    }
                ]
            },
            {
                "peed_ele_col": [
                    {
                        "text": "CSP",
                        "icon": "icon-csp-lblue"
                    },
                    {
                        "text": "Database",
                        "icon": "icon-database-solid"
                    },
                    {
                        "text": "Email",
                        "icon": "icon-email"
                    },
                    {
                        "text": "Fast Food",
                        "icon": "icon-fastfood"
                    }
                ]
            },
            {
                "peed_ele_col": [
                    {
                        "text": "Image",
                        "icon": "icon-image"
                    },
                    {
                        "text": "School",
                        "icon": "icon-school"
                    },
                    {
                        "text": "Language",
                        "icon": "icon-language"
                    },
                    {
                        "text": "No",
                        "icon": "icon-no"
                    }
                ]
            },
        ],
        "peed_fld": [
            {
                "number": "2.",
                "title": "Sensory"
            }
        ],
        "peed_ele_master": [
            {
                "text": "I",
                        "icon": "icon-Autistic-Person"
            },
            {
                "text": "Audio Desc",
                        "icon": "icon-audio-description"
            },
            {
                "text": "Account",
                        "icon": "icon-account_circle"
            },
            {
                "text": "Add box",
                        "icon": "icon-add_box"
            },
            {
                "text": "Add",
                        "icon": "icon-add"
            },
            {
                "text": "Apps",
                        "icon": "icon-apps-24px"
            },
            {
                "text": "Bar Chart",
                        "icon": "icon-bar_chart"
            },
            {
                "text": "Camera",
                        "icon": "icon-camera_alt"
            },
            {
                "text": "Tick",
                        "icon": "icon-check-circle-together"
            },
            {
                "text": "Cross",
                        "icon": "icon-close"
            },
            {
                "text": "Smile",
                        "icon": "icon-comment-alt-smile"
            },
            {
                "text": "Compass",
                        "icon": "icon-compass"
            },
            {
                "text": "CSP",
                        "icon": "icon-csp-lblue"
            },
            {
                "text": "Database",
                        "icon": "icon-database-solid"
            },
            {
                "text": "Email",
                        "icon": "icon-email"
            },
            {
                "text": "Fast Food",
                        "icon": "icon-fastfood"
            },
            {
                "text": "Image",
                        "icon": "icon-image"
            },
            {
                "text": "School",
                        "icon": "icon-school"
            },
            {
                "text": "Language",
                        "icon": "icon-language"
            },
            {
                "text": "No",
                        "icon": "icon-no"
            }
        ],

    }
    stepper_object = Stepper.Stepper(request)

    stepper_object.update()

    auth_url = OpenHumansMember.get_auth_url()
    context = {**context, **{'auth_url': auth_url}}  # ,
#                             'oh_proj_page': settings.OH_PROJ_PAGE}}
    if request.user.is_authenticated:
        return redirect('overview')
    # return render(request, 'index.html', context=context)

#    if(page == "error"):
#        raise Http404("page does not exist: error")
#    else:
    return render(request, 'split.html', context=context)


def componentGallery(request):
    context = {
        "stepper": [
            {
                "id": 1,
                "label": "Login"
            },
            {
                "id": 2,
                "label": "Define Profile"
            },
            {
                "id": 3,
                "label": "Add Event"
            }
        ],
        "ueftext": [
            {
                "rows": [
                    {
                        "qtext": "Where",
                        "qcolour": "#4d75ad",
                        "phtext": "Enter name of location or postcode...",
                        "input": "ip"

                    }
                ],
                "maintext": "Where..."
            },
            {
                "rows": [
                    {
                        "qtext": "What",
                        "qcolour": "#ffbb5d",
                        "phtext": "Your experience can be entered here...",
                        "input": "ta"
                    }
                ],
                "maintext": "Enter your experience"
            },
            {
                "rows": [
                    {
                        "qtext": "What",
                        "qcolour": "#ffbb5d",
                        "phtext": "",
                        "input": "ta"
                    }
                ],
                "maintext": "What would you have wished to be different?"
            }
        ],
    "user_exp": [
            {
                "id": "32097868",
                "datetime": "Sept 18, 2019, 10:31 a.m.",
                "user_txt": [
                    {
                        "question": "Event",
                        "text": "The air conditioning in the room where I was having a meeting was really loud and I found it really hard to concentrate."
                    },
                    {
                        "question": "What would you have liked to be different?",
                        "text": ""
                    }
                ]
            },
            {
                "id": "19279611",
                "datetime": "Sept 17, 2019, 8:46 a.m.",
                "user_txt": [
                    {
                        "question": "Event",
                        "text": "The tube is too loud."
                    },
                    {
                        "question": "What would you have liked to be different?",
                        "text": ""
                    }
                ]
            },
            {
                "id": "32097868",
                "datetime": "Sept 17, 2019, 8:45 a.m.",
                "user_txt": [
                    {
                        "question": "Event",
                        "text": "I'm at a conference today and I found people not using the microphone really difficult - it makes it much harder to concentrate on what they were saying. I was much more distracted."
                    },
                    {
                        "question": "What would you have liked to be different?",
                        "text": ""
                    }
                ]
            }
        ],
        "MONE_data": [
            {
                "UID": "0000001",
                "EID": "32097868",
                "date": "18/09/19",
                "Event_What": "The air conditioning in the room where I was having a meeting was really loud and I found it really heard to concentrate, it was a rubbish experience.",
                "Location_Where": "NW1 2HS",
                "LikeToBeDifferent": "I would have liked the air conditioning to less loud to aid my concentration",
                "Summary": "Loud Air Conditioning"
            },
            {
                "UID": "0000002",
                "EID": "32097867",
                "date": "17/09/19",
                "Event_What": "The tube is too loud.",
                "Location_Where": "NW1 8NH",
                "LikeToBeDifferent": "would have liked the tube to be less loud",
                "Summary": "Loud Tube"
            },
            {
                "UID": "0000003",
                "EID": "32097866",
                "date": "17/09/19",
                "Event_What": "I'm at a conference today and I found the people not using the microphone really difficult - it makes it harder to concentrate on what they were saying. I was much more distracted.",
                "Location_Where": "SE15 5DQ",
                "LikeToBeDifferent": "For people in conferences to use a microphone. To aid my concentration and reduce my distraction.",
                "Summary": "None use of microphone in conference"
            }
        ],
        "Documentation_data":[
            {
            "ID": "0000001",
            "Date": "14/06/2019",
            "Group": "moderation",
            "Name": "experience-moderation-guidlines",
            "Version": "0.4"
            },
            {
            "ID": "0000002",
            "Date": "02/09/2020",
            "Group": "moderation",
            "Name": "why-is-there-a-moderation-process",
            "Version": "1"
            },
            {
            "ID": "0000003",
            "Date": "09/11/2020",
            "Group": "instructional",
            "Name": "experience-creation-and-submission",
            "Version": "2"
            },
        ],
        'AP_data': [
            {
                "Title": "Navigation Adjustment",
                "ID": "navadjust",
                "arrow": "arrow_expandingpanel_na"
            },
            {
                "Title": "Colour Adjustment",
                "ID": "coladjust",
                "arrow": "arrow_expandingpanel_ca"
            },
            {
                "Title": "Content Adjustment",
                "ID": "contadjust",
                "arrow": "arrow_expandingpanel_cta"
            }
        ],
        'AP_blank':
            {
                "Title": "Expanding Panel",
                "ID": "blankexpanel",
                "arrow": "arrow_expandingpanel_bep",
                "content": "Content that can be replaced"
        },
        'AP_gallery_panels':
            {
                "Title": "Panel Components - These components are based on core Bootstap components and form the core structural elements of the platform.",
                "ID": "gal_expanel_panels",
                "arrow": "arrow_expandingpanel_bep"
        },
        'AP_gallery_animated_panels':
            {
                "Title": "Animated Panel Components - These components are animated using javascript to show and hide them. They are core structural elements of the platform.",
                "ID": "gal_expanel_animated_panel",
                "arrow": "arrow_expandingpanel_bep"
        },
            'AP_gallery_navigation':
            {
                "Title": "Navigation Components - These components are used for platform navigation, they allow the platform user to move around the available sections/pages of the platform and to other related content.",
                "ID": "gal_expanel_navigation",
                "arrow": "arrow_expandingpanel_bep"
        },
        'AP_HCL':
            {
                "Desc": "Some people cannot read text if there is not sufficient contrast between the text and background. For others, bright colours (high luminance) are not readable; they need low luminance."
        },
        "peed_ele_row": [
            {
                "peed_ele_col": [
                    {
                        "text": "I",
                        "icon": "icon-Autistic-Person"
                    },
                    {
                        "text": "Audio Desc",
                        "icon": "icon-audio-description"
                    },
                    {
                        "text": "Account",
                        "icon": "icon-account_circle"
                    },
                    {
                        "text": "Add box",
                        "icon": "icon-add_box"
                    }
                ]
            },
            {
                "peed_ele_col": [
                    {
                        "text": "Add",
                        "icon": "icon-add"
                    },
                    {
                        "text": "Apps",
                        "icon": "icon-apps-24px"
                    },
                    {
                        "text": "Bar Chart",
                        "icon": "icon-bar_chart"
                    },
                    {
                        "text": "Camera",
                        "icon": "icon-camera_alt"
                    }
                ]
            },
            {
                "peed_ele_col": [
                    {
                        "text": "Tick",
                        "icon": "icon-check-circle-together"
                    },
                    {
                        "text": "Cross",
                        "icon": "icon-close"
                    },
                    {
                        "text": "Smile",
                        "icon": "icon-comment-alt-smile"
                    },
                    {
                        "text": "Compass",
                        "icon": "icon-compass"
                    }
                ]
            },
            {
                "peed_ele_col": [
                    {
                        "text": "CSP",
                        "icon": "icon-csp-lblue"
                    },
                    {
                        "text": "Database",
                        "icon": "icon-database-solid"
                    },
                    {
                        "text": "Email",
                        "icon": "icon-email"
                    },
                    {
                        "text": "Fast Food",
                        "icon": "icon-fastfood"
                    }
                ]
            },
            {
                "peed_ele_col": [
                    {
                        "text": "Image",
                        "icon": "icon-image"
                    },
                    {
                        "text": "School",
                        "icon": "icon-school"
                    },
                    {
                        "text": "Language",
                        "icon": "icon-language"
                    },
                    {
                        "text": "No",
                        "icon": "icon-no"
                    }
                ]
            },
        ],
        "peed_fld": [
            {
                "number": "2.",
                "title": "Sensory"
            }
        ],
        "peed_ele_master": [
            {
                "text": "I",
                        "icon": "icon-Autistic-Person"
            },
            {
                "text": "Audio Desc",
                        "icon": "icon-audio-description"
            },
            {
                "text": "Account",
                        "icon": "icon-account_circle"
            },
            {
                "text": "Add box",
                        "icon": "icon-add_box"
            },
            {
                "text": "Add",
                        "icon": "icon-add"
            },
            {
                "text": "Apps",
                        "icon": "icon-apps-24px"
            },
            {
                "text": "Bar Chart",
                        "icon": "icon-bar_chart"
            },
            {
                "text": "Camera",
                        "icon": "icon-camera_alt"
            },
            {
                "text": "Tick",
                        "icon": "icon-check-circle-together"
            },
            {
                "text": "Cross",
                        "icon": "icon-close"
            },
            {
                "text": "Smile",
                        "icon": "icon-comment-alt-smile"
            },
            {
                "text": "Compass",
                        "icon": "icon-compass"
            },
            {
                "text": "CSP",
                        "icon": "icon-csp-lblue"
            },
            {
                "text": "Database",
                        "icon": "icon-database-solid"
            },
            {
                "text": "Email",
                        "icon": "icon-email"
            },
            {
                "text": "Fast Food",
                        "icon": "icon-fastfood"
            },
            {
                "text": "Image",
                        "icon": "icon-image"
            },
            {
                "text": "School",
                        "icon": "icon-school"
            },
            {
                "text": "Language",
                        "icon": "icon-language"
            },
            {
                "text": "No",
                        "icon": "icon-no"
            }
        ],
        "navlinks": [
            {
                "linkTitle": "Home",
                "linkLoc": "/home",
                "linkName": "home",
                "template": "home.html"
            },
            {
                "linkTitle": "About",
                "linkLoc": "/about",
                "linkName": "about",
                "template": "about.html"
            },
            {
                "linkTitle": "Share",
                "linkLoc": "/share",
                "linkName": "share",
                "template": "share.html"
            },
            {
                "linkTitle": "Login",
                "linkLoc": "/login",
                "linkName": "login",
                "template": "login.html"
            }
        ],
    }

    stepper_object = Stepper.Stepper(request)

    stepper_object.update()

    auth_url = OpenHumansMember.get_auth_url()
    context = {**context, **{'auth_url': auth_url}}  # ,
#               'oh_proj_page': settings.OH_PROJ_PAGE}}
    if request.user.is_authenticated:
        oh_member = request.user.openhumansmember
        context = {**context, **{'oh_id': oh_member.oh_id,
                                 'oh_member': oh_member}}  # ,
#                                 'oh_proj_page': settings.OH_PROJ_PAGE}}

    return render(request, 'gallery.html', context=context)


def share(request):
    context = {
        "ueftext": [
        {
            "rows": [
            {
                "qtext": "Where",
                "qcolour": "#4d75ad",
                "phtext": "Enter name of location or postcode...",
                "input": "ip"

            }
            ],
            "maintext": "Where..."
        },
        {
            "rows": [
            {
                "qtext": "What",
                "qcolour": "#ffbb5d",
                "phtext": "Your experience can be entered here...",
                "input": "ta"
            }
            ],
            "maintext": "Enter your experience"
        },
        {
            "rows": [
            {
                 "qtext": "What",
                 "qcolour": "#ffbb5d",
                 "phtext": "",
                 "input": "ta"
            }
            ],
                "maintext": "What would you have wished to be different?"
        }
        ]
    }
    return render(request, 'share.html', context=context)

def moderationreject(request):
    context = {
    'mrtext': [
        {
            "rows": [
                {
                    "qtext": "",
                    "qcolour": "#4d75ad",
                    "phtext": "Enter reasoning",
                    "input": "ta"
                }
            ],
            "maintext": "Why is this experience not appropriate?"
        },
        {
            "rows": [
                {
                    "qtext": "",
                    "qcolour": "#4d75ad",
                    "phtext": "Enter proposed changes",
                    "input": "ta"
                }
           ],
            "maintext": "How can this experience be improved?"
        }
    ]
    }
    return render(request, 'moderationreject.html', context=context)




def configure(request):
    return render(request, 'configure.html')

def getinvolved(request):
    return render(request, 'getinvolved.html')


def view(request):
    context = {
        "stepper": [
            {
                "id": 1,
                "label": "Login"
            },
            {
                "id": 2,
                "label": "Define Profile"
            },
            {
                "id": 3,
                "label": "Add Experience"
            },
            {
                "id": 4,
                "label": "View Experience"
            }
        ],
    }
    stepper_object = Stepper.Stepper(request)

    stepper_object.update()
    return render(request, 'view.html', context=context)


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def mydata(request):
    context = {
        "user_exp": [
            {
                "id": "32097868",
                "datetime": "Sept 18, 2019, 10:31 a.m.",
                "user_txt": [
                    {
                        "question": "Event",
                        "text": "The air conditioning in the room where I was having a meeting was really loud and I found it really hard to concentrate."
                    },
                    {
                        "question": "What would you have liked to be different?",
                        "text": ""
                    }
                ]
            },
            {
                "id": "19279611",
                "datetime": "Sept 17, 2019, 8:46 a.m.",
                "user_txt": [
                    {
                        "question": "Event",
                        "text": "The tube is too loud."
                    },
                    {
                        "question": "What would you have liked to be different?",
                        "text": ""
                    }
                ]
            },
            {
                "id": "32097868",
                "datetime": "Sept 17, 2019, 8:45 a.m.",
                "user_txt": [
                    {
                        "question": "Event",
                        "text": "I'm at a conference today and I found people not using the microphone really difficult - it makes it much harder to concentrate on what they were saying. I was much more distracted."
                    },
                    {
                        "question": "What would you have liked to be different?",
                        "text": ""
                    }
                ]
            }
        ]
    }
    return render(request, 'mydata.html', context=context)

def moderation(request):
    context = {
        "MONE_data": [
            {
                "UID": "0000001",
                "EID": "32097868",
                "date": "18/09/19",
                "Event_What": "The air conditioning in the room where I was having a meeting was really loud and I found it really heard to concentrate, it was a rubbish experience.",
                "Location_Where": "NW1 2HS",
                "LikeToBeDifferent": "I would have liked the air conditioning to less loud to aid my concentration",
                "Summary": "Loud Air Conditioning"
            },
            {
                "UID": "0000002",
                "EID": "32097867",
                "date": "17/09/19",
                "Event_What": "The tube is too loud.",
                "Location_Where": "NW1 8NH",
                "LikeToBeDifferent": "would have liked the tube to be less loud",
                "Summary": "Loud Tube"
            },
            {
                "UID": "0000003",
                "EID": "32097866",
                "date": "17/09/19",
                "Event_What": "I'm at a conference today and I found the people not using the microphone really difficult - it makes it harder to concentrate on what they were saying. I was much more distracted.",
                "Location_Where": "SE15 5DQ",
                "LikeToBeDifferent": "For people in conferences to use a microphone. To aid my concentration and reduce my distraction.",
                "Summary": "None use of microphone in conference"
            }

        ],
        "AP_data": [
            {
                "Title": "Navigation Adjustment",
                "ID": "navadjust",
                "arrow": "arrow_expandingpanel_na"
            },
            {
                "Title": "Colour Adjustment",
                "ID": "coladjust",
                "arrow": "arrow_expandingpanel_ca"
            },
            {
                "Title": "Content Adjustment",
                "ID": "contadjust",
                "arrow": "arrow_expandingpanel_cta"
            }
        ],
        "AP_blank":
            {
                "Title": "Expanding Panel",
                "ID": "blankexpanel",
                "arrow": "arrow_expandingpanel_bep"
            },
        "AP_HCL":
            {
                "Desc": "Some people cannot read text if there is not sufficient contrast between the text and background. For others, bright colours (high luminance) are not readable; they need low luminance."
            }
    }

    stepper_object = Stepper.Stepper(request)

    stepper_object.update()

    auth_url = OpenHumansMember.get_auth_url()
    context = {**context, **{'auth_url': auth_url}}#,
#               'oh_proj_page': settings.OH_PROJ_PAGE}}
    if request.user.is_authenticated:
        oh_member = request.user.openhumansmember
        context = {**context, **{'oh_id': oh_member.oh_id,
                                 'oh_member': oh_member}}#,
#                                 'oh_proj_page': settings.OH_PROJ_PAGE}}

    return render(request, 'gallery.html', context=context)

def moderationreject(request):
    context = {
    'mrtext': [
        {
            "rows": [
                {
                    "qtext": "",
                    "qcolour": "#4d75ad",
                    "phtext": "Enter reasoning",
                    "input": "ta"
                }
            ],
            "maintext": "Why is this experience not appropriate?"
        },
        {
            "rows": [
                {
                    "qtext": "",
                    "qcolour": "#4d75ad",
                    "phtext": "Enter proposed changes",
                    "input": "ta"
                }
           ],
            "maintext": "How can this experience be improved?"
        }
    ]
    }
    return render(request, 'moderationreject.html', context=context)

def configure(request):
    return render(request, 'configure.html')


def getinvolved(request):
    return render(request, 'getinvolved.html')

def view(request):
    context = {
        "stepper": [
            {
                "id": 1,
                "label": "Login"
            },
            {
                "id": 2,
                "label": "Define Profile"
            },
            {
                "id": 3,
                "label": "Add Experience"
            },
            {
                "id": 4,
                "label": "View Experience"
            }
        ],
    }
    stepper_object = Stepper.Stepper(request)

    stepper_object.update()
    return render(request, 'view.html', context=context)


def mydata(request):
    context = {
        "user_exp": [
            {
                "id": "32097868",
                "datetime": "Sept 18, 2019, 10:31 a.m.",
                "user_txt": [
                    {
                        "question": "Event",
                        "text": "The air conditioning in the room where I was having a meeting was really loud and I found it really hard to concentrate."
                    },
                    {
                        "question": "What would you have liked to be different?",
                        "text": ""
                    }
                ]
            },
            {
                "id": "19279611",
                "datetime": "Sept 17, 2019, 8:46 a.m.",
                "user_txt": [
                    {
                        "question": "Event",
                        "text": "The tube is too loud."
                    },
                    {
                        "question": "What would you have liked to be different?",
                        "text": ""
                    }
                ]
            },
            {
                "id": "32097868",
                "datetime": "Sept 17, 2019, 8:45 a.m.",
                "user_txt": [
                    {
                        "question": "Event",
                        "text": "I'm at a conference today and I found people not using the microphone really difficult - it makes it much harder to concentrate on what they were saying. I was much more distracted."
                    },
                    {
                        "question": "What would you have liked to be different?",
                        "text": ""
                    }
                ]
            }
        ]
    }
    return render(request, 'mydata.html', context=context)

def moderation(request):
    context = {
        "MONE_data": [
            {
                "UID": "0000001",
                "EID": "32097868",
                "date": "18/09/19",
                "Event_What": "The air conditioning in the room where I was having a meeting was really loud and I found it really heard to concentrate, it was a rubbish experience.",
                "Location_Where": "NW1 2HS",
                "LikeToBeDifferent": "I would have liked the air conditioning to less loud to aid my concentration",
                "Summary": "Loud Air Conditioning"
            },
            {
                "UID": "0000002",
                "EID": "32097867",
                "date": "17/09/19",
                "Event_What": "The tube is too loud.",
                "Location_Where": "NW1 8NH",
                "LikeToBeDifferent": "would have liked the tube to be less loud",
                "Summary": "Loud Tube"
            },
            {
                "UID": "0000003",
                "EID": "32097866",
                "date": "17/09/19",
                "Event_What": "I'm at a conference today and I found the people not using the microphone really difficult - it makes it harder to concentrate on what they were saying. I was much more distracted.",
                "Location_Where": "SE15 5DQ",
                "LikeToBeDifferent": "For people in conferences to use a microphone. To aid my concentration and reduce my distraction.",
                "Summary": "None use of microphone in conference"
            }
        ]
    }
    return render(request, 'moderation.html', context=context)

def accessibility_settings(request):
    return render(request, 'settings.html')



def login(request):
    return render(request, 'login.html')


def overview(request):
    if request.user.is_authenticated:
        oh_member = request.user.openhumansmember
        context = {'oh_id': oh_member.oh_id,
                   'oh_member': oh_member,
                   'oh_proj_page': settings.OH_PROJ_PAGE}
        return render(request, 'overview.html', context=context)
    return redirect('index')


def pictorialexperienceeditor(request):
    context = {
        "peed_ele_row": [
            {
                "peed_ele_col": [
                    {
                        "text": "I",
                        "icon": "icon-Autistic-Person"
                    },
                    {
                        "text": "Audio Desc",
                        "icon": "icon-audio-description"
                    },
                    {
                        "text": "Account",
                        "icon": "icon-account_circle"
                    },
                    {
                        "text": "Add box",
                        "icon": "icon-add_box"
                    }
                ]
            },
            {
                "peed_ele_col": [
                    {
                        "text": "Add",
                        "icon": "icon-add"
                    },
                    {
                        "text": "Apps",
                        "icon": "icon-apps-24px"
                    },
                    {
                        "text": "Bar Chart",
                        "icon": "icon-bar_chart"
                    },
                    {
                        "text": "Camera",
                        "icon": "icon-camera_alt"
                    }
                ]
            },
            {
                "peed_ele_col": [
                    {
                        "text": "Tick",
                        "icon": "icon-check-circle-together"
                    },
                    {
                        "text": "Cross",
                        "icon": "icon-close"
                    },
                    {
                        "text": "Smile",
                        "icon": "icon-comment-alt-smile"
                    },
                    {
                        "text": "Compass",
                        "icon": "icon-compass"
                    }
                ]
            },
            {
                "peed_ele_col": [
                    {
                        "text": "CSP",
                        "icon": "icon-csp-lblue"
                    },
                    {
                        "text": "Database",
                        "icon": "icon-database-solid"
                    },
                    {
                        "text": "Email",
                        "icon": "icon-email"
                    },
                    {
                        "text": "Fast Food",
                        "icon": "icon-fastfood"
                    }
                ]
            },
            {
                "peed_ele_col": [
                    {
                        "text": "Image",
                        "icon": "icon-image"
                    },
                    {
                        "text": "School",
                        "icon": "icon-school"
                    },
                    {
                        "text": "Language",
                        "icon": "icon-language"
                    },
                    {
                        "text": "No",
                        "icon": "icon-no"
                    }
                ]
            },
        ],
        "peed_fld": [
            {
                "number": "2.",
                "title": "Sensory"
            }
        ],
        "peed_ele_master": [
            {
                "text": "I",
                        "icon": "icon-Autistic-Person"
            },
            {
                "text": "Audio Desc",
                        "icon": "icon-audio-description"
            },
            {
                "text": "Account",
                        "icon": "icon-account_circle"
            },
            {
                "text": "Add box",
                        "icon": "icon-add_box"
            },
            {
                "text": "Add",
                        "icon": "icon-add"
            },
            {
                "text": "Apps",
                        "icon": "icon-apps-24px"
            },
            {
                "text": "Bar Chart",
                        "icon": "icon-bar_chart"
            },
            {
                "text": "Camera",
                        "icon": "icon-camera_alt"
            },
            {
                "text": "Tick",
                        "icon": "icon-check-circle-together"
            },
            {
                "text": "Cross",
                        "icon": "icon-close"
            },
            {
                "text": "Smile",
                        "icon": "icon-comment-alt-smile"
            },
            {
                "text": "Compass",
                        "icon": "icon-compass"
            },
            {
                "text": "CSP",
                        "icon": "icon-csp-lblue"
            },
            {
                "text": "Database",
                        "icon": "icon-database-solid"
            },
            {
                "text": "Email",
                        "icon": "icon-email"
            },
            {
                "text": "Fast Food",
                        "icon": "icon-fastfood"
            },
            {
                "text": "Image",
                        "icon": "icon-image"
            },
            {
                "text": "School",
                        "icon": "icon-school"
            },
            {
                "text": "Language",
                        "icon": "icon-language"
            },
            {
                "text": "No",
                        "icon": "icon-no"
            }
        ],

    }

    return render(request, 'pictorialexperienceeditor.html', context=context)


def logout_user(request):
    """
    Logout user
    """
    if request.method == 'GET':
        logout(request)
    return redirect('index')


def upload(request):
    if request.method == 'POST':
        print(request.POST)
        experience_text = request.POST.get('experience')
        wish_different_text = request.POST.get('wish_different')
        viewable = request.POST.get('viewable')
        if not viewable:
            viewable = 'not public'
        research = request.POST.get('research')
        if not research:
            research = 'non-research'

        if experience_text:
            experience_id = str(uuid.uuid1())
            output_json = {
                'text': experience_text,
                'wish_different': wish_different_text,
                'timestamp': str(datetime.datetime.now())}
            output = io.StringIO()
            output.write(json.dumps(output_json))
            output.seek(0)
            metadata = {'tags': [viewable, research],
                        'uuid': experience_id,
                        'description': 'this is a test file'}
            request.user.openhumansmember.upload(
                stream=output,
                filename='testfile.json',
                metadata=metadata)
            if viewable == 'viewable':
                PublicExperience.objects.create(
                    experience_text=experience_text,
                    difference_text=wish_different_text,
                    open_humans_member=request.user.openhumansmember,
                    experience_id=experience_id)
        return redirect('index')
    else:

        # if request.user.is_authenticated:
        return render(request, 'main/upload.html')
    return redirect('index')


def list_files(request):
    if request.user.is_authenticated:
        context = {'files': request.user.openhumansmember.list_files()}
        return render(request, 'list.html',
                      context=context)
    return redirect('index')


def list_public_experiences(request):
    experiences = PublicExperience.objects.filter(approved='approved')
    return render(
        request,
        'public_experiences.html',
        context={'experiences': experiences})


def moderate_public_experiences(request):
    experiences = PublicExperience.objects.filter(approved='not reviewed')
    return render(
        request,
        'old/moderate_public_experiences.html',
        context={'experiences': experiences})


def review_experience(request, experience_id):
    experience = PublicExperience.objects.get(experience_id=experience_id)
    print(experience)
    experience.approved = 'approved'
    experience.save()
    print(experience.approved)
    return redirect('moderate_public_experiences')


def make_non_viewable(request, oh_file_id, file_uuid):
    pe = PublicExperience.objects.get(experience_id=file_uuid)
    pe.delete()
    oh_files = request.user.openhumansmember.list_files()
    for f in oh_files:
        if str(f['id']) == str(oh_file_id):
            experience = requests.get(f['download_url']).json()
            new_metadata = f['metadata']
            new_metadata['tags'] = ['not public'] + f['metadata']['tags'][1:]
            output = io.StringIO()
            output.write(json.dumps(experience))
            output.seek(0)
            request.user.openhumansmember.upload(
                stream=output,
                filename='testfile.json',
                metadata=new_metadata)
            request.user.openhumansmember.delete_single_file(
                file_id=oh_file_id)
    return redirect('list')


def make_viewable(request, oh_file_id, file_uuid):
    oh_files = request.user.openhumansmember.list_files()
    for f in oh_files:
        if str(f['id']) == str(oh_file_id):
            experience = requests.get(f['download_url']).json()
            new_metadata = f['metadata']
            new_metadata['tags'] = ['viewable'] + f['metadata']['tags'][1:]
            output = io.StringIO()
            output.write(json.dumps(experience))
            output.seek(0)
            request.user.openhumansmember.upload(
                stream=output,
                filename='testfile.json',
                metadata=new_metadata)
            request.user.openhumansmember.delete_single_file(
                file_id=oh_file_id)
            PublicExperience.objects.create(
                experience_text=experience['text'],
                difference_text=experience['wish_different'],
                open_humans_member=request.user.openhumansmember,
                experience_id=file_uuid)
    return redirect('list')


def make_non_research(request, oh_file_id, file_uuid):
    oh_files = request.user.openhumansmember.list_files()
    for f in oh_files:
        if str(f['id']) == str(oh_file_id):
            experience = requests.get(f['download_url']).json()
            new_metadata = f['metadata']
            new_metadata['tags'] = f['metadata']['tags'][:-1] + \
                ['non-research']
            output = io.StringIO()
            output.write(json.dumps(experience))
            output.seek(0)
            request.user.openhumansmember.upload(
                stream=output,
                filename='testfile.json',
                metadata=new_metadata)
            request.user.openhumansmember.delete_single_file(
                file_id=oh_file_id)
    return redirect('list')


def make_research(request, oh_file_id, file_uuid):
    oh_files = request.user.openhumansmember.list_files()
    for f in oh_files:
        if str(f['id']) == str(oh_file_id):
            experience = requests.get(f['download_url']).json()
            new_metadata = f['metadata']
            new_metadata['tags'] = f['metadata']['tags'][:-1] + ['research']
            output = io.StringIO()
            output.write(json.dumps(experience))
            output.seek(0)
            request.user.openhumansmember.upload(
                stream=output,
                filename='testfile.json',
                metadata=new_metadata)
            request.user.openhumansmember.delete_single_file(
                file_id=oh_file_id)
    return redirect('list')
