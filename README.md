# Image2map

Image2map is an utility that allows you to generate Leaflet based interactives maps from plain images.

This utility automates the process to generate an interactive map from a 2D image. It raster image tiles for use with Leaflet in addition to build minimum files and required libraries to get everything you need to deploy your web interactive map.

[Live demo](https://luisdavidfer.github.io/image2map/demo/).

## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have installed Python 3.
* You have installed [Python3-gdal](https://github.com/OSGeo/gdal).

## How to use

To get help about commands and options run:
```
$ python3 image2map.py -h
```

For basic usage run:
```
$ python3 image2map.py <map_name> <image_path> <image_width> <image_height>
```

Multicore process to raster image tiles is available running:
```
$ python3 image2map.py -mp <map_name> <image_path> <image_width> <image_height>
```

For example [demo](https://luisdavidfer.github.io/image2map/demo/):
```
$ python3 image2map.py -mp "Middle Earth" ./middle-earth.jpg 7970 5500
```


## Built with

* [Leaflet](https://github.com/Leaflet/Leaflet): JavaScript library for mobile-friendly interactive maps. Licensed under [BSD 2-Clause "Simplified" License](https://github.com/Leaflet/Leaflet/blob/master/LICENSE).
* [Gdal2tiles-leaflet](https://github.com/commenthol/gdal2tiles-leaflet): Modified version of [gdal2tiles.py](https://github.com/OSGeo/gdal/blob/master/gdal/swig/python/scripts/gdal2tiles.py) which adds support for raster images as plain 2D maps in leafletjs. Licensed under [MIT License](https://github.com/commenthol/gdal2tiles-leaflet/blob/master/LICENSE).
* [Leaflet-rastercoords](https://github.com/commenthol/leaflet-rastercoords): Leaflet plugin for plain image map projection to display large images using tiles generated with [gdal2tiles-leaflet](https://github.com/commenthol/gdal2tiles-leaflet). Licensed under [MIT License](https://github.com/commenthol/gdal2tiles-leaflet/blob/master/LICENSE).


## License

This project is available as open source under the terms of the [MIT License](https://github.com/luisdavidfer/image2map/blob/master/LICENSE).
