var citizenSciencePlatform_slidingpanelfunctions = {
  OpenPanel: function (panelID, opts) {
    try {
      switch (document.getElementById(panelID).getAttribute('data-direction')) {
      case "left":
        document
          .getElementById(panelID)
          .classList.add("sliding-panel-open-left");
        break;
      case "right":
        document
          .getElementById(panelID)
          .classList.add("sliding-panel-open-right");
        break;
      case "top":
        break;
      case "bottom":
        break;
      default:
        document
          .getElementById(panelID)
          .classList.add("sliding-panel-open-right");
    }
    } catch (error) {
        document
          .getElementById(panelID)
          .classList.add("sliding-panel-open-right");
    }
    
  },
  ClosePanel: function (panelID) {
    var count;
    for (count = 0; count < 4; count++) {
      try {
        switch (count) {
          case 0:
              document
              .getElementById(panelID)
              .classList.remove("sliding-panel-open-left");
            break;
          case 1:
              document
              .getElementById(panelID)
              .classList.remove("sliding-panel-open-right");
            break;
          case 2:
              document
              .getElementById(panelID)
              .classList.remove("sliding-panel-open-top");
            break;
          case 4:
              document
              .getElementById(panelID)
              .classList.remove("sliding-panel-open-bottom");
            break;
        }
      } 
      catch (error){

      }
  
    }
  },
};
