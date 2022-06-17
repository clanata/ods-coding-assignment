function setStations(search) {
    const url = window.location.href + "stations/" + search + "/";
    const stations = document.getElementById("stations");
    var options = '';
    fetch(url)
      .then(response => response.json())
      .then(data => {
        data.stations.forEach(function(station) {
            options += '<option value="' + station + '" />';
        });
        stations.innerHTML = options;
    });
}

const origin_input = document.getElementById("id_origin_full_name");
const destination_input = document.getElementById("id_destination_full_name");
origin_input.addEventListener("input", (event) => setStations(event.target.value));
destination_input.addEventListener("input", (event) => setStations(event.target.value));

