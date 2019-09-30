from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from api import preexisting_models


class NeighborhoodUnitsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = preexisting_models.NeighborhoodUnits
        fields = '__all__'
        geo_field = 'wkb_geometry'

class BuildingFootprintsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = preexisting_models.BuildingFootprints 
        fields = '__all__'
        geo_field = 'wkb_geometry'

class CensusBgAoiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.CensusBgAoi
        fields = '__all__'
        geo_field = 'wkb_geometry'

class CommunityCentersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.CommunityCenters
        fields = '__all__'
        geo_field = 'wkb_geometry'

class CountiesAoiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.CountiesAoi
        fields = '__all__'
        geo_field = 'wkb_geometry'

class HospitalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.Hospital
        fields = '__all__'
        geo_field = 'wkb_geometry'

class OregonLiquefactionSusceptibilitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.OregonLiquefactionSusceptibility
        fields = '__all__'
        geo_field = 'wkb_geometry'

class OregonNehrpSiteClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.OregonNehrpSiteClass
        fields = '__all__'
        geo_field = 'wkb_geometry'

class OregonVsMeasurementIntervalsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.OregonVsMeasurementIntervals
        fields = '__all__'
        geo_field = 'wkb_geometry'

class OregonVsMeasurementSitesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.OregonVsMeasurementSites
        fields = '__all__'
        geo_field = 'wkb_geometry'

class SubstationPortlandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.SubstationPortland
        fields = '__all__'
        geo_field = 'wkb_geometry'

class UnreinforcedMasonryBuildingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.UnreinforcedMasonryBuildings
        fields = '__all__'
        geo_field = 'wkb_geometry'

class ElectricalTransmissionStructuresSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.ElectricalTransmissionStructures
        fields = '__all__'
        geo_field = 'wkb_geometry'

class HydrantsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.Hydrants
        fields = '__all__'
        geo_field = 'wkb_geometry'

class JurisdictionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.Jurisdictions
        fields = '__all__'
        geo_field = 'wkb_geometry'

class QuakeLossViewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.QuakeLossView
        fields = '__all__'

class PhfM6P8BedrockGroundmotionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.PhfM6P8BedrockGroundmotion
        fields = '__all__'
        geo_field = 'wkb_geometry'

class PointsOfServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.PointsOfService
        fields = '__all__'

class PopulationAndBuildingDensitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.PopulationAndBuildingDensity
        fields = '__all__'
        geo_field = 'wkb_geometry'

class PressureZonesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.PressureZones
        fields = '__all__'
        geo_field = 'wkb_geometry'

class PressurizedMainsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.PressurizedMains
        fields = '__all__'
        geo_field = 'wkb_geometry'

class RegionalDrinkingWaterAdvisoryBoundarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.RegionalDrinkingWaterAdvisoryBoundary
        fields = '__all__'
        geo_field = 'wkb_geometry'

class RegionalWaterDistrictsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.RegionalWaterDistricts
        fields = '__all__'
        geo_field = 'wkb_geometry'

class ServicesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.Services
        fields = '__all__'
        geo_field = 'wkb_geometry'

class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.Address
        fields = '__all__'
        geo_field = 'wkb_geometry'

class FireStaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.FireSta
        fields = '__all__'
        geo_field = 'wkb_geometry'
		
class SchoolsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.Schools
        fields = '__all__'
        geo_field = 'wkb_geometry'

class NeighborhoodsRegionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.NeighborhoodsRegions
        fields = '__all__'


class MajorRiverBridgesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.MajorRiverBridges
        fields = '__all__'
        geo_field = 'wkb_geometry'

class BasicEarthquakeEmergencyCommunicationNodeBeecnLocationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.BasicEarthquakeEmergencyCommunicationNodeBeecnLocations
        fields = '__all__'
        geo_field = 'wkb_geometry'

class RlisSt180520Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.RlisSt180520
        fields = '__all__'
        geo_field = 'wkb_geometry'

class POISerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.POI
        fields = '__all__'
        geo_field = 'wkb_geometry'

class DisasterNeighborhoodsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = preexisting_models.DisasterNeighborhoods
        fields = '__all__'

class DisasterNeighborhoodViewSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = preexisting_models.DisasterNeighborhoodView
        fields = '__all__'
        geo_field = 'wkb_geometry'

class DisasterNeighborhoodGridSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = preexisting_models.DisasterNeighborhoodGrid
        fields = '__all__'
        geo_field = 'wkb_geometry'

class AebmResultsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = preexisting_models.AebmResults
        fields = '__all__'
        geo_field = 'wkb_geometry'

class OptimizedAebmResultsSerializer(serializers.Serializer):
    class Meta:
        model = preexisting_models.AebmResults
        fields = '__all__'
        geo_field = 'wkb_geometry'
        read_only_fields = fields
        
