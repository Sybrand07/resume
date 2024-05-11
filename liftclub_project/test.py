<!DOCTYPE html>
<html>
<head>
  <title>Select Your Pickup, Checkpoint, and Destination Locations</title>
  <!-- Load the Google Maps JavaScript API with your API key -->
  <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap" async defer></script>
  <script>
    // Initialize the map and other variables
    var map, pickupMarker, destinationMarker, checkpointMarker;
    var directionsService, directionsRenderer;

    function initMap() {
      map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: -33.918861, lng: 18.423300},
        zoom: 12
      });

      directionsService = new google.maps.DirectionsService();
      directionsRenderer = new google.maps.DirectionsRenderer();
      directionsRenderer.setMap(map);

      map.addListener('click', function(event) {
        var locationType = document.getElementById('pickupButton').classList.contains('active') ? 'pickup' : 
                           document.getElementById('destinationButton').classList.contains('active') ? 'destination' : 
                           'checkpoint';
        placeMarker(event.latLng, locationType);
      });

      toggleButton('pickup');
    }

    function placeMarker(location, locationType) {
      if (locationType === 'pickup' && pickupMarker) {
        pickupMarker.setMap(null);
      } else if (locationType === 'destination' && destinationMarker) {
        destinationMarker.setMap(null);
      } else if (locationType === 'checkpoint' && checkpointMarker) {
        checkpointMarker.setMap(null);
      }
      
      var iconUrl = locationType === 'pickup' ? 'http://maps.google.com/mapfiles/ms/icons/green-dot.png' : 
                    locationType === 'destination' ? 'http://maps.google.com/mapfiles/ms/icons/red-dot.png' :
                    'http://maps.google.com/mapfiles/ms/icons/yellow-dot.png';
      
      var marker = new google.maps.Marker({
        position: location,
        map: map,
        icon: iconUrl
      });

      if (locationType === 'pickup') {
        pickupMarker = marker;
      } else if (locationType === 'destination') {
        destinationMarker = marker;
      } else if (locationType === 'checkpoint') {
        checkpointMarker = marker;
      }
      
      if (pickupMarker && destinationMarker) {
        calculateAndDisplayRoute();
      }
    }

    function calculateAndDisplayRoute() {
      var start = pickupMarker.getPosition();
      var end = destinationMarker.getPosition();
      var waypoint = checkpointMarker ? [{ location: checkpointMarker.getPosition(), stopover: true }] : [];

      directionsService.route({
        origin: start,
        destination: end,
        waypoints: waypoint,
        optimizeWaypoints: true,
        travelMode: 'DRIVING'
      }, function(response, status) {
        if (status === 'OK') {
          directionsRenderer.setDirections(response);
        } else {
          window.alert('Directions request failed due to ' + status);
        }
      });
    }

    function toggleButton(locationType) {
      var pickupButton = document.getElementById('pickupButton');
      var destinationButton = document.getElementById('destinationButton');
      var checkpointButton = document.getElementById('checkpointButton');
      
      pickupButton.classList.remove('active');
      destinationButton.classList.remove('active');
      checkpointButton.classList.remove('active');

      if (locationType === 'pickup') {
        pickupButton.classList.add('active');
      } else if (locationType === 'destination') {
        destinationButton.classList.add('active');
      } else if (locationType === 'checkpoint') {
        checkpointButton.classList.add('active');
      }
    }
  </script>
  <style>
    #map {
      height: 400px;
      width: 100%;
    }

    .button-container {
      text-align: center;
    }

    .location-button {
      display: inline-block;
      margin: 10px;
      padding: 10px 20px;
      font-size: 16px;
      cursor: pointer;
      border: 1px solid black;
      border-radius: 5px;
    }

    .location-button.active {
      background-color: #4CAF50;
      color: white;
    }

    .button-separator {
      border-top: 1px dashed black;
      margin: 5px;
      width: 50px;
    }
  </style>
</head>
<body>
  <h1>Select Your Pickup, Checkpoint, and Destination Locations</h1>
  <div class="button-container">
    <button id="pickupButton" class="location-button" onclick="toggleButton('pickup')">Pickup</button>
    <div class="button-separator"></div>
    <button id="checkpointButton" class="location-button" onclick="toggleButton('checkpoint')">Checkpoint</button>
    <div class="button-separator"></div>
    <button id="destinationButton" class="location-button" onclick="toggleButton('destination')">Destination</button>
  </div>
  <div id="map"></div>
</body>
</html>
