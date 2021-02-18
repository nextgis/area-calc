import json
from calculate_area import *

f_inputname = 'test.geojson'

with open(f_inputname) as f:
    d = json.load(f)

for f in d['features']:
    points = []
    geom = f['geometry']['coordinates']
    for pnt in geom[0]:
        points.append(pnt)
    
    area = areacalc(points)
    print(area)