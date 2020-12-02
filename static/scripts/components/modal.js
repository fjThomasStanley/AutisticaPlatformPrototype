var citizenSciencePlatform_modalfunctions = {
  ShowModal: function (modalID) {
    document.getElementById(modalID).style.display = "block";
    var height = document.getElementById(showImageUpload).getAttribute('data-height');
    var width = document.getElementById(showImageUpload).getAttribute('data-width');
    if (height == "")
    {
        height = "250";
    }
    if (width == "")
    {
        width = "300";
    }
    document.documentElement.style.setProperty("--md-height") = height + "px";
    document.documentElement.style.setProperty("--md-width") = width + "px";
    document.documentElement.style.setProperty("--md-top") = "-" + toString(parseInt(height)/2) + "px";
    document.documentElement.style.setProperty("--md-left") = "-" + toString(parseInt(width)/2) + "px";
  },  },

  HideModal: function (modalID) {
    document.getElementById(modalID).style.display = "none";
  }
};
