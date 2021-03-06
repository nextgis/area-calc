# area-calc
Ellipsoidal area calculation reproduced in Python with no dependencies

# usage

```python
from calculate_area import areacalc
p0 = [51.82, 63.8]
p1 = [43.48, 55.62]
p2 = [75.38, 59.13]
p3 = [51.82, 63.8]

points = [p0,p1,p2,p3]

areacalc(points)
>730215205638.4752
```

# Notes
Implementations and code in other software, languages

* NGQ 2.x [QgsDistanceArea::computePolygonArea](https://github.com/nextgis/nextgisqgis/blob/424126701151c25879a8ecfb17b387a346129f1c/src/core/qgsdistancearea.cpp#L889)
* QGIS 3.x [QgsDistanceArea::computePolygonArea](https://github.com/qgis/QGIS/blob/master/src/core/qgsdistancearea.cpp#L1022)
* GRASS [G_ellipsoid_polygon_area](https://github.com/OSGeo/grass/blob/53eda832018485b0d02f94755c8cca9c499c528d/lib/gis/area_poly1.c)
* pyproj [geod_geninverse_int](https://github.com/OSGeo/PROJ/blob/2414eb2bb655588b4b7e9fe86bba70592bd7f911/src/geodesic.c#L674) -> [geod_polygon_compute](https://github.com/OSGeo/PROJ/blob/2414eb2bb655588b4b7e9fe86bba70592bd7f911/src/geodesic.c#L1842) -> [geod_polygonarea](https://github.com/OSGeo/PROJ/blob/2414eb2bb655588b4b7e9fe86bba70592bd7f911/src/geodesic.c#L1948) -> [_polygon_area_perimeter](https://github.com/pyproj4/pyproj/blob/17886ea3a8b0aac9cc1f7d33275e8e2850a65463/pyproj/_geod.pyx#L266) -> [geometry_area_perimeter](https://github.com/pyproj4/pyproj/blob/17886ea3a8b0aac9cc1f7d33275e8e2850a65463/pyproj/geod.py#L517), [Geodesic Routines Description](https://github.com/OSGeo/PROJ/blob/master/src/geodesic.h#L1948), [Docs](https://pyproj4.github.io/pyproj/stable/api/geod.html#pyproj.Geod.geometry_area_perimeter)
* NextGIS Frontend [JS](https://github.com/nextgis/nextgis_frontend/tree/master/packages/area)


