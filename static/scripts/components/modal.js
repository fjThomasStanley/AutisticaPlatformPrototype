var citizenSciencePlatform_modalfunctions = {
  ShowModal: function (modalID) {
    document.getElementById(modalID).style.display = "block";

    var height = document.getElementById("showImageUpload").getAttribute("data-height");

    var width = document.getElementById("showImageUpload").getAttribute('data-width');
    if (height == "")
    {
        height = "250";
    }

    if (width == "")
    {
        width = "300";
    }

    document.documentElement.style.setProperty("--md-height", height + "px");
    document.documentElement.style.setProperty("--md-width", width + "px");
    document.documentElement.style.setProperty("--md-top", "-" + (parseInt(height) / 2).toString() + "px");
    document.documentElement.style.setProperty("--md-left", "-" + (parseInt(width) / 2).toString() + "px");
  },

  HideModal: function (modalID) {
    document.getElementById(modalID).style.display = "none";
  }
};
