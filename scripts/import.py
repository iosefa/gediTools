import time

from gediTools.controller import  DatabaseDroid

start = time.time()
droid = DatabaseDroid(database_url='postgresql://admin:password@localhost:5432/gedi')
droid.l2b_2_postgis('/media/iosefa/data/GEDI02_B_002/', 'gedi02b_base', 'gedi02b_geolocation',
                   'gedi02b_ancillary', 'gedi02b_land_cover', 'gedi02b_rx_processing', clean=True)
end = time.time()

print(end-start)
"""
    Gets download links for granules within a bounding box and temporal range.

A shapefile can be uploaded with a query to restrict results to those that overlap the geometry in the shapefile. Note that unlike the spatial parameters, geometry in the shapefile is OR'd together, not AND'd. So if a collection overlaps any of the geometry in the shapefile it will match. Note also that the shapefile parameter supports shapefiles containing polygons with holes.

Currently the only supported shapefile formats are ESRI, KML, and GeoJSON. For ESRI all the sub-files (*.shp, *.shx, etc.) must be uploaded in a single zip file.

Shapefiles are limited to 5000 points by default. A user using a shapefile with more points than the CMR supported limit can use the simplify-shapefile parameter to request that the CMR try to simplify (reduce the number of points) the shapefile so that it is under the limit.


The following limits apply to uploaded shapefiles:
* Shapefiles are limited in size to 1,000,000 bytes.
* Shapefiles are limited to 500 features
* Shapefiles are limited to 5000 points.

Regarding polygon ring winding, ESRI shapefiles must follow the ESRI standard, i.e., exterior (boundary) rings are clockwise, and holes are counter-clockwise. GeoJSON must follow the RFC7946 specification, i.e., exterior rings are counterclockwise, and holes are clockwise. KML must follow the KML 2.2 specification, i.e., all polygon rings are counter-clockwise.

Shapefile upload is only supported using POST with multipart/form-data and the mime type for the shapefile must be given as application/shapefile+zip, application/geo+json, or application/vnd.google-earth.kml+xml.



:param product:
:param download_path:
:param start_date:
:param end_date:
:param bbox:
:param shapefile:
:param variable_subset:
"""