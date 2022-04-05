$(document).ready(function () {
  var currentLocation = window.location.href.split("/")[3];
  if (currentLocation == "") {
    currentLocation = "home";
  }
  var menuid = "#nav-" + currentLocation;
  $(function () {
    $(".nav a").removeClass("active");
    $(menuid).addClass("active");
  });
});
