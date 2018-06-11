from rest_framework_gis.serializers import GeoFeatureModelSerializer

from rest_framework.serializers import ModelSerializer

from .models import POI

class POISerializer(GeoFeatureModelSerializer):
    class Meta:
        model = POI
        fields = '__all__'
        geo_field = 'wkb_geometry'

