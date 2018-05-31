

function update() {
var field = document.getElementById("test");
field.innerHtml="dfdfdssa2222222222222222222222fsf";

}

setTimeout(function() {
  update();
}, 30000);


$(document).ready(function() {
    $.ajax({
      url: `https://www.prevision-meteo.ch/services/json/lat=46.259lng=5.235`,
      type: 'GET',
      data: {
        format: 'json'
      },
      success: function(response) {
        $('.showHumidity').text(`The humidity in ${city} is ${response.main.humidity}%`);
        $('.showTemp').text(`The temperature in Kelvins is ${response.main.temp}.`);
      },
      error: function() {
        $('#errors').text("There was an error processing your request. Please try again.")
      }
    });

});
