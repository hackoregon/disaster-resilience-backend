from rest_framework.decorators import api_view
from django.contrib.gis.geos import GEOSGeometry, MultiPoint, MultiPolygon, MultiLineString
from .models import POI
from .serializers import POISerializer
from .helpers import sandbox_view_factory
from .meta import poi_meta

poi = sandbox_view_factory(
  model_class=POI,
  serializer_class=POISerializer,
  multi_geom_class=MultiPoint,
  geom_field='wkb_geometry',
  attributes =poi_meta['attributes'],
  dates=poi_meta['dates'],
  )
