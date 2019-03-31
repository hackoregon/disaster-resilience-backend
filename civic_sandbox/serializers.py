from rest_framework_gis.serializers import GeoFeatureModelSerializer

from rest_framework.serializers import HyperlinkedModelSerializer

from .models import POI, DisasterNeighborhoodView, Slide, Foundation, Packages

class POISerializer(GeoFeatureModelSerializer):
    class Meta:
        model = POI
        fields = '__all__'
        geo_field = 'wkb_geometry'

class ShakingSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = DisasterNeighborhoodView
        fields = ('id', 'name', 'pgv_site_mean_mmi_txt', 'pgv_site_mean_desc')
        geo_field = 'wkb_geometry'

class LiquefactionSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = DisasterNeighborhoodView
        fields = ('id', 'name', 'pgd_total_wet_mean_di')
        geo_field = 'wkb_geometry'

class LandslideSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = DisasterNeighborhoodView
        fields = ('id', 'name', 'pgd_landslide_dry_mean_di')
        geo_field = 'wkb_geometry'

class CensusResponseSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = DisasterNeighborhoodView
        fields = ('id', 'name', 'census_response_rate')
        geo_field = 'wkb_geometry'

class SlideSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Slide
        fields = '__all__'

class FoundationSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Foundation
        fields = '__all__'

class PackageSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Packages
        fields = '__all__'
        depth = 1
