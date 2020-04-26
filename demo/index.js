// Map properties
let map = L.map("map", {
    minZoom: 2,
    maxZoom: 5,
    zoomControl: false
});
// Controls properties
L.control.zoom({position:"bottomright"}).addTo(map);
// Image properties
let img = new L.RasterCoords(map, [7970,5500]);
// Tiles properties
L.tileLayer('tiles/{z}/{x}/{y}.png', {
    noWrap: true,
    attribution: '<a title="Leaflet plugin for plain image map projection to display large images using tiles generated with gdal2tiles-leaflet" href="https://github.com/commenthol/leaflet-rastercoords">Leaflet-rastercoords</a>' + ' | ' + '<a title="Generate raster image tiles for use with Leaflet" href="https://github.com/commenthol/gdal2tiles-leaflet">Gdal2tiles-leaflet</a>' + ' | ' + '<a title="Python 3 utility to generate Leaflet based interactives maps from plain images." href="https://www.github.com/luisdavidfer/image2map">Image2map</a>'
}).addTo(map);
// Map initial view
map.setView(img.unproject([img.width/2, img.height/2]), 3);
