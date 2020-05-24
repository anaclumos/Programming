function stopie() {
  var ua = window.navigator.userAgent;
  var msie = ua.indexOf("MSIE ");
  if (msie > 0 || !!navigator.userAgent.match(/Trident.*rv\:11\./)) {
    var r = confirm("You are using IE. Edge Browser Highly Recommended. Checkout Edge?");
    if (r == true) {
      url = window.location.href;
      command = "Edge" + window.location.href;
      var shell = new ActiveXObject("WScript.Shell");
      shell.run(command);
    }
  }
}

stopie();