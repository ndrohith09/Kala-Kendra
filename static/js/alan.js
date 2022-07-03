var alanBtnInstance = alanBtn({
    key: "75415e2067d1e9af77a686833ab7743e2e956eca572e1d8b807a3e2338fdd0dc/stage",
    onCommand: function (commandData) { 
        if (commandData.command === "captiongenerator") {
            window.location.href = "/#art-form";
        } 

        if (commandData.command === "art1") {
            window.location.href = "/#art-form";
        }

      if (commandData.command === "captiongenerator") {
          window.location.href = "/#caption-form";
      }
    },
    rootEl: document.getElementById("alan-btn"),
  });