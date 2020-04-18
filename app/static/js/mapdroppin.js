var directionsDisplay;
var map;
var endMarker;

function initialize() {
  // Get input fields
  var latlon_input = document.getElementById("latlon");
  var lat_input = document.getElementById("lat");
  var lon_input = document.getElementById("lon");
  var type_input = document.getElementById("tyyppi");

  // Init vars
  var location = null;
  var mapOptions = null;
  var lat = null;
  var lon = null;

  // No spot location. Use default location
  location = new google.maps.LatLng(50.395346, 8.667042);
  mapOptions = {
    zoom: 3,
    center: location
  }

  // Get spot location from latlon input field
  if (latlon_input != undefined){
    if(latlon.value != ''){
      var lat_lon = latlon.value.split(',');
      lat = lat_lon[0];
      lon = lat_lon[1];
      location = new google.maps.LatLng(lat, lon);
      mapOptions = {
        zoom: 12,
        center: location
      }
    }
  } 

  // Get lat & lon from separate input fields
  if (lat_input != undefined && lon_input != undefined){
    if(lat_input.value != '' || lon_input.value != ''){
      lat = lat_input.value;
      lon = lon_input.value;
      location = new google.maps.LatLng(lat, lon);
      mapOptions = {
        zoom: 12,
        center: location
      }
    }
  }
  // For countries and towns zoom out
  if(type_input == undefined){
    location = new google.maps.LatLng(lat, lon);
    mapOptions = {
      zoom: 5,
      center: location
    }
  }

  // create map
  map = new google.maps.Map(document.getElementById("map"), mapOptions);

  // create marker for spot. not country or town!
  if(type_input != undefined){
    endMarker = new google.maps.Marker({
      position: new google.maps.LatLng(lat, lon),
      map: map
    });
  }
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
    latlon.value = endMarker.getPosition().lat() + ',' +  endMarker.getPosition().lng();
  }
  var lat = document.getElementById("lat");
  var lon = document.getElementById("lon");
  if (lat != undefined && lon != undefined){
    lat.value = endMarker.getPosition().lat();
    lon.value = endMarker.getPosition().lng();
  }
}

google.maps.event.addDomListener(window, 'load', initialize);
