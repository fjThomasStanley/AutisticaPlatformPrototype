Components description


# Panel Components
These components are based on core Bootstap components and form the core structural elements of the platform.





## Secondary banner
This component is used to display a tagline to the user, it provides a short description about what the page is about and how the user should be expected to interact with the page

### Template Inclusion

Template name: [banner.html](/./skeleton/templates/components/partials/banner.html) 

```
{% include 'pathToComponentTemplate' %} 
```

To customise the banner message systemwide please refer to the django.po file in the locale folder. Please adjust the msgstr value that corresponds with the msgid of 'Tagline'.




## Jumbotron
This component is used to show key and important information. This component is created using the Bootstrap library

### Template inclusion
Template name: [jumbotron.html](/./skeleton/templates/components/partials/jumbotron.html) 

```
{% include 'pathToComponentTemplate' %} 
```

To customise the jumbotron




## Card
This component is used to show key and important information. This component 


### Template inclusion

Template name: []


```HTML
<div class="card autistica-card" style="width: 40rem;">
    <div class="card-body">
      <h4 class="card-title hiw-heading">Title</h4>
      <div class="hiw-body">
        Card Body
      </div>
    </div>
</div>
```







# Animated Panel Components
These components are animated using javascript to show and hide them. They are core structural elements of the platform.




## Modular Alert 
This component alets the user to a specific piece of information. It is used to provide a warning, error a general information message.

### Template Inclusion

Template name: [modularalerts.html](/./skeleton/templates/components/modularalerts.html) 


This component only needs to be included once in the web application
```
{% include 'pathToComponentTemplate' with modalID=value %} 
```

This component is driven by javascript, please ensure the related javascript files are include in the application root template (views.py render page). For multiple instances of the component only one instance of the javascript files are required as they globally generic. 

- /static/scripts/components/modal.js


### Parameters

| Parameter Name   |  Purpose | Requirment | Value |
| :-------------   | :---------- | :-------------   | :---------- |
| ModalID | The unique ID for the component, used by javascript to select component from other components on the page | Required | String - Alphanumeric. As it is an ID, it must be unique to the component. |

### Functions


<table>
        <tr>
            <th>Function Parameter</th>
            <th>Purpose</th>
            <th>Data</th>
        </tr>
        <tr>
            <td>1</td>
            <td>Title of the modular alert</td>
            <td>String - Alphanumeric Text</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Alert text of the modular alert. The body of the modular alert</td>
            <td>String - Alphanumeric Text</td>
        </tr>
        <tr>
            <td>3</td>
            <td>The type of icon displayed in the modular alert</td>
            <td>
                Number:
                <br>
                1 - Alert
                <br>
                2 - Warning
                <br>
                3 - Info
                <br>
                Default value: Warning
            </td>
        </tr>
        <tr>
            <th colspan="3">Example</th>
        </tr>
        <tr>
            <td colspan="3">
                showModularAlert('Timeout Save', 'Inactive for 10 minutes, in 2 minutes time your event will be saved as a draft', 1)
            </td>
        </tr>
        <tr>
            <th colspan="3">Notes</th>
        </tr>
        <tr>
            <td colspan="3">
                The modular alert is a typeof modal component. The modal component requires a modalID to enable the functionality of showing the modal (the modular alert component). Therefore when including the modular alert component within your template you must use the following django tag structure:
                <br>
                <br>
                {{"{% include 'pathToComponentTemplate' with modalID=value %}"}}
            </td>
        </tr>
</table>






## Image Upload
This component allows the user to upload media into the platform. A typical use case of this component is to submit images alongside an experience submission.

### Template Inclusion



Template name: [imageupload.html](/./skeleton/templates/components/imageupload.html) 



This component is driven by javascript, please ensure the related javascript files are include in the application root template (views.py render page). For multiple instances of the component only one instance of the javascript files are required as they globally generic. 

- /static/scripts/components/modal.js
- /static/scripts/components/attachdropzone.js
- /static/scripts/dropzone.js



## Accessibility Panel
This component allows the user to adjust accessibility settings so that platform can be displayed to the user in the most accessible way.

### Template Inclusion

Template name: [accessibilitypanel.html](/./skeleton/templates/components/accessibilitypanel.html) 


This component is driven by javascript, please ensure the related javascript files are include in the application root template (views.py render page). For multiple instances of the component only one instance of the javascript files are required as they globally generic. 

- /static/scripts/components/slidingpanel.js

## Expanding Panel
This component is used to contain content in an expandable and collapsible panel. The expanding panel allows the user to hide specific elements of the page if there is too much content being shown.

### Template Inclusion

Template name: [expandingpanel.html](/./skeleton/templates/components/partials/expandingpanel.html) 

### Parameters

<table>
        <tr>
            <th>Parameter Name</th>
            <th>Purpose</th>
            <th>Requirment</th>
            <th>Value</th>
        </tr>
        <tr>
            <td>PanelData</td>
            <td>The required configuration information for the expanding panel component</td>
            <td>Required</td>
            <td>Object[ExpandingPanelData]<td>
        </tr>
</table>

### ObjectTypes

<table>
    <tr>
        <th>ObjectType</th>
        <th>Infomation</th>
    <tr>
    <tr>
        <td>ExpandingPanelData</td>
        <td>
        <table>
        <tr>
            <th>Property</th>
            <th>Purpose</th>
            <th>Requirment</th>
            <th>Value</th>
        </tr>
        <tr>
            <td>title</td>
            <td>The title value displayed in the expanding panel header</td>
            <td>Required</td>
            <td>String - Alphanumeric<td>
        </tr>
        <tr>
            <td>ID</td>
            <td>The unique name given to the component intance so that it can be referenced by javascript code
            <td>Required</td>
            <td>String</td>
        </tr>
        <tr>
            <td>content</td>
            <td>The value that will displayed in main body of the expanding panel component</td>
            <td>Optional</td>
            <td>String</td>
        </tr>
        </table>
        </td>
    </tr>
</table>

### Child Components

<table>
    <tr>
        <th>Component Name</th>
        <th>Purpose</th>
        <th>TemplateName</th>
    </tr>
    <tr>
        <td>colouradjustment</td>
        <td>Used on the accessibility panel to adjust platform colours for accessibility</td>
        <td>[colouradjustment.html](/./skeleton/templates/components/colouradjustment.html)</td>
    </tr>
    <tr>
        <td>navadjustment</td>
        <td>Used on the accessibility panel to adjust how navigation guidance is provided for accessibility</td>
        <td>[contentadjustment.html](/./skeleton/templates/components/navadjustment.html)</td>
    </tr>
</table>


# Navigation Components
These components are used for platform navigation, they allow the platform user to move around the available sections/pages of the platform and to other related content.



## Navigation Bar
The navigation bar allows the user to navigate between the different pages and available functions of the platform

### Template Inclusion


Template name: [navbar.html](/./skeleton/templates/components/navbar.html) 

The context variable in the views.py requires a property called navlinks which should contain an array of NavLink objects. Each navlink object defined in navlinks will add a navigatable link to the navigation bar.

### ObjectTypes

<table>
    <tr>
        <th>ObjectType</th>
        <th>Infomation</th>
    <tr>
    <tr>
        <td>Navlink</td>
        <td>
        <table>
        <tr>
            <th>Property</th>
            <th>Purpose</th>
            <th>Requirment</th>
            <th>Value</th>
        </tr>
        <tr>
            <td>linkTitle</td>
            <td>A name for the link that is displayed to the user in the navigation bar</td>
            <td>Required</td>
            <td>String - Alphanumeric<td>
        </tr>
        <tr>
            <td>linkLoc</td>
            <td>The location the link should navigate to</td>
            <td>Required</td>
            <td>String</td>
        </tr>
        <tr>
            <td>linkName</td>
            <td>The name of the link that is used to compare the currently navigated page. If current page is equal then this adds selected class.</td>
            <td>Required</td>
            <td>String</i></td>
        </tr>
        <tr>
            <td>template</td>
            <td>The template file for the page that should be rendered in the application when the link is navigated to.</td>
            <td>Required</td>
            <td>String</td>
        </tr>
        </table>
        </td>
    </tr>
</table>



## Footer
The footer links to relevant resources that the user can navigate to

### Template Inclusion

Template name: [footer.html](/./skeleton/templates/components/footer.html) 



# Interactive form components



## User Journey Stepped Control
This control allows a user to step though a staged process such as an experience entry. It allows a larger process to be broken down into smaller manageable steps and this control provides the visual feedback to the user about which stage in the process they are currently on and how many stages there are in total.




--------------------------


## Newsletter Cards

### Template Inclusion

Template name: [newsletterCards.html](/./skeleton/templates/components/newsletterCards.html) 


## Newsletter Signup
This control allows a user to signup to platform communications so that they can be kept informed about platform developments. 

### Template Inclusion

Template name: [newsletterSignup.html](/./skeleton/templates/components/newsletterSignup.html) 

## Language Selector
This control allows a user to switch the platform to a different language 

### Template Inclusion

Template name: [languageSelector.html](/./skeleton/templates/components/languageSelector.html) 

## Define Profile
This component allows a user to select the type of user they are so that the platform can be best tailored towards their use case.

### Template Inclusion

Template name: [defineprofile.html](/./skeleton/templates/components/defineprofile.html) 


## User Experience Form
This component allows a user to provide details about an experience so that it can be submitted into the platform.

### Template Inclusion

Template name: [userexperienceform.html](/./skeleton/templates/components/userexperienceform.html) 


## Experience Viewer Control
This component allows users to see their previously submitted experiences and to view the publicly shared experiences of other users.

### Template Inclusion

Template name: [experienceviewercontrol.html](/./skeleton/templates/components/experienceviewercontrol.html) 


## Community Approval Mechanism
This component allows platform moderators to manage the shared experiences from users and moderate the experiences into the publicly viewable list.

### Template Inclusion

Template name: [communityapprovalmechanism.html](/./skeleton/templates/components/communityapprovalmechanism.html) 

## Moderation of New Experiences
This component allows platform moderators to manage the shared experiences from users and moderate the experiences into the publicly viewable list.

### Template Inclusion

Template name: [moderationofnewexperiences.html](/./skeleton/templates/components/moderationofnewexperiences.html) 


## Documentation Viewer
This component allows the user to see general documentation about the platform such as community guidlines and assistive help guides.

### Template Inclusion

Template name: [documentationviewer.html](/./skeleton/templates/components/documentationviewer.html) 

## Pictorial Experience Editor
This component allows a user to submit an experience using images or symbols as opposed to text based. This component aims to assist those who struggle with writing to share their experiences.

### Template Inclusion

Template name: [pictorialexperienceeditor.html](/./skeleton/templates/components/pictorialexperienceeditor.html) 