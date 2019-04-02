from rest_framework.decorators import api_view
from django.contrib.gis.geos import GEOSGeometry, MultiPoint, MultiPolygon, MultiLineString
from .models import POI, DisasterNeighborhoodView
from .serializers import POISerializer, ShakingSerializer, LandslideSerializer, LiquefactionSerializer, CensusResponseSerializer
from .helpers import sandbox_view_factory
from .meta import poi_meta, shaking_meta, landslide_meta, liquefaction_meta, census_response_meta
from rest_framework import viewsets
from civic_sandbox import models
from civic_sandbox import serializers
from django.http import JsonResponse
from civic_sandbox import packages


poi = sandbox_view_factory(
  model_class=POI,
  serializer_class=POISerializer,
  multi_geom_class=MultiPoint,
  geom_field='wkb_geometry',
  attributes =poi_meta['attributes'],
  dates=poi_meta['dates'],
  )

shaking = sandbox_view_factory(
  model_class=DisasterNeighborhoodView,
  serializer_class=ShakingSerializer,
  multi_geom_class=MultiPolygon,
  geom_field='wkb_geometry',
  attributes =shaking_meta['attributes'],
  dates=shaking_meta['dates'],
  )

liquefaction = sandbox_view_factory(
  model_class=DisasterNeighborhoodView,
  serializer_class=LiquefactionSerializer,
  multi_geom_class=MultiPolygon,
  geom_field='wkb_geometry',
  attributes =liquefaction_meta['attributes'],
  dates=liquefaction_meta['dates'],
  )


landslide = sandbox_view_factory(
  model_class=DisasterNeighborhoodView,
  serializer_class=LandslideSerializer,
  multi_geom_class=MultiPolygon,
  geom_field='wkb_geometry',
  attributes =landslide_meta['attributes'],
  dates=landslide_meta['dates'],
  )

censusresponse = sandbox_view_factory(
  model_class=DisasterNeighborhoodView,
  serializer_class=CensusResponseSerializer,
  multi_geom_class=MultiPolygon,
  geom_field='wkb_geometry',
  attributes =census_response_meta['attributes'],
  dates=census_response_meta['dates'],
  )

class SlideSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows SlideSet to be viewed or listed.
    """
    queryset = models.Slide.objects.all()
    serializer_class = serializers.SlideSerializer

class FoundationSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows FoundationSet to be viewed or listed.
    """
    queryset = models.Foundation.objects.all()
    serializer_class = serializers.FoundationSerializer

class PackagesSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows PackageSet to be viewed or listed.
    """
    queryset = models.Packages.objects.all()
    serializer_class = serializers.PackageSerializer

def packages_view(request):
    return JsonResponse(packages.package_info)
