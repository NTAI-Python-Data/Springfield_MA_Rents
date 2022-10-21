
import os

zipcode_shapes_dir = r'C:\Users\PowerUser\Desktop\00_PythonWIP_2022\!0_Rents_Swiss_Dashboard\massachusetts_zipcodes_nt'

townsurvey_shapes_dir = r'C:\Users\PowerUser\Desktop\00_PythonWIP_2022\!0_Rents_Swiss_Dashboard\ma_townssurvey_shp\townssurvey_shp'

mass_shape_file = 'ZIPCODES_NT_POLY.shp'

TOWNSSURVEY_POLYM = 'TOWNSSURVEY_POLYM.shp'

TOWNSSURVEY_POLY = 'TOWNSSURVEY_POLY.shp'

os.chdir(townsurvey_shapes_dir)


import shapefile
from json import dumps

# read the shapefile
reader = shapefile.Reader(TOWNSSURVEY_POLY)
fields = reader.fields[1:]
field_names = [field[0] for field in fields]
buffer = []
for sr in reader.shapeRecords():
    atr = dict(zip(field_names, sr.record))
    geom = sr.shape.__geo_interface__
    buffer.append(dict(type="Feature", \
    geometry=geom, properties=atr))

    # write the GeoJSON file

geojson = open("TOWNSSURVEY_POLY.json", "w")
geojson.write(dumps({"type": "FeatureCollection", "features": buffer}, indent=2) + "\n")
geojson.close()


