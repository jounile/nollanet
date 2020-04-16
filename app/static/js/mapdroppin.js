var directionsDisplay;
var map;
var endMarker;
function initialize() {
  var helsinki = new google.maps.LatLng(60.186427, 24.934886);
  var mapOptions = {
    zoom: 5,
    center: helsinki
  }
  map = new google.maps.Map(document.getElementById("map"), mapOptions);
  directionsDisplay.setMap(map);
}
function dropPin() {
  // if any previous marker exists, let's first remove it from the map
  if (endMarker) {
    endMarker.setMap(null);
  }
  // create the marker
  endMarker = new google.maps.Marker({
    position: map.getCenter(),
    map: map,
    draggable: true,
  });
  copyMarkerpositionToInput();
  // add an event "onDrag"
  google.maps.event.addListener(endMarker, 'dragend', function() {
    copyMarkerpositionToInput();
  });
}
function copyMarkerpositionToInput() {
  // get the position of the marker, and set it as the value of input
  var latlon = document.getElementById("latlon");
  if (latlon != undefined){
    latlon.value = endMarker.getPosition().lat() +','+  endMarker.getPosition().lng();
  }
  var lat = document.getElementById("lat");
  var lon = document.getElementById("lon");
  if (lat != undefined && lon != undefined){
    lat.value = endMarker.getPosition().lat();
    lon.value = endMarker.getPosition().lng();
  }
}

google.maps.event.addDomListener(window, 'load', initialize);
