$(document).ready(function() {
  var toogle = document.getElementById("fullscreenToggle");
  toogle.addEventListener("click", toggleFullscreen);

  function isNotFullScreen() {
    return !document.fullscreenElement && !document.mozFullScreenElement &&
        !document.webkitFullscreenElement && !document.msFullscreenElement
  }
  
  function toggleFullscreen() {
    var elem = document.documentElement
    console.log(elem);
    // for newer Webkit and Firefox
    var requestFullScreen = 
           elem.requestFullScreen
        || elem.webkitRequestFullScreen
        || elem.mozRequestFullScreen
        || elem.msRequestFullScreen;
    var exitFullScreen = 
          document.cancelFullScreen
        || document.msExitFullScreen
        || document.mozCancelFullScreen
        || document.webkitCancelFullScreen;
    if(typeof requestFullScreen !="undefined" && requestFullScreen){
      console.log("Newer Web");      
      if (isNotFullScreen()) {
        console.log("Not FullScreen");
        requestFullScreen.call(elem);
      } else {
        console.log("FullScreen");
        exitFullScreen.call(document);
      }
    } else if(typeof window.ActiveXObject!="undefined"){
      console.log("for Internet Explorer");
      var wscript = new ActiveXObject("WScript.Shell");
      if (wscript!=null) {
         wscript.SendKeys("{F11}");
      }
    } else {
      console.log("Something is undefined please check again browser policy to FullScreen");
    }
  }
  
});
