
var map = L.map("map").setView([27.2,83.95], 12);

var osm = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
})

var forest = L.tileLayer('https://{s}.tile.thunderforest.com/transport-dark/{z}/{x}/{y}.png?apikey={apikey}', {
	attribution: '&copy; <a href="http://www.thunderforest.com/">Thunderforest</a>, &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
	maxZoom: 22
});
var dark = L.tileLayer('https://tile.jawg.io/jawg-dark/{z}/{x}/{y}{r}.png?access-token={accessToken}', {
	attribution: '<a href="https://jawg.io" title="Tiles Courtesy of Jawg Maps" target="_blank">&copy; <b>Jawg</b>Maps</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
	minZoom: 0,
	maxZoom: 22,
});
var tomtom = L.tileLayer('https://{s}.tile.thunderforest.com/spinal-map/{z}/{x}/{y}.png?apikey={apikey}', {
	attribution: '&copy; <a href="http://www.thunderforest.com/">Thunderforest</a>, &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
	maxZoom: 22
});

var layers = {
    "osm":osm,
    "forest":forest,
    "dark": dark,
    "tomtom":tomtom
}



var marker1 = L.marker([27.8,83.90], {
    title:"My Home",
    draggable:true,
    opacity: 0.5
}).addTo(map).bindPopup("<div style = 'width:'500px; over-flow:'hidden''><h1>Marker</h1><p>Welcome to my homeaddddddddadaddddddddddddddddddddddd</p><img src = './download.jpg'  / ><div>").openPopup();
var marker2 = L.marker([27.4,83.88], {
    title:"My Home",
    draggable:true,
    opacity: 0.5
}).addTo(map).bindPopup("<div style = 'width:'500px; over-flow:'hidden''><h1>Marker</h1><p>Welcome to my homeaddddddddadaddddddddddddddddddddddd</p><img src = './download.jpg'  / ><div>").openPopup();
var marker3 = L.marker([27.6,83.75], {
    title:"My Home",
    draggable:true,
    opacity: 0.5
}).addTo(map).bindPopup("<div style = 'width:'500px; over-flow:'hidden''><h1>Marker</h1><p>Welcome to my homeaddddddddadaddddddddddddddddddddddd</p><img src = './download.jpg'  / ><div>").openPopup();

var markers = L.layerGroup([marker1, marker2, marker3]);
var overLayers = {
    "markers":markers,
    "marker1": marker1,
    "marker2":marker2,
    "marker3":marker3
}

L.control.layers(layers, overLayers,).addTo(map);
var geojson = L.geoJSON(nepalData, {
    onEachFeature: function(feature, layer)
    {
        var districtName = feature.properties.DISTRICT;
        layer.bindPopup(`District: ${districtName}`)
    },
    style:{
        color:"red",
        fillColor:'pink',
        fillOpacity:'0.5'
    }
}).addTo(map);
