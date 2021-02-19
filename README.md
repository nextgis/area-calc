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
Implementations in other software, languages

* NGQ 2.x [QgsDistanceArea::computePolygonArea](https://github.com/nextgis/nextgisqgis/blob/424126701151c25879a8ecfb17b387a346129f1c/src/core/qgsdistancearea.cpp#L889)
* MASTER 3.x [QgsDistanceArea::computePolygonArea](https://github.com/qgis/QGIS/blob/master/src/core/qgsdistancearea.cpp#L1022)
* GRASS [G_ellipsoid_polygon_area](https://github.com/OSGeo/grass/blob/53eda832018485b0d02f94755c8cca9c499c528d/lib/gis/area_poly1.c)


