from django.contrib.gis.db import models

class POI(models.Model): 
    pk_id= models.CharField(primary_key=True, max_length=30,)
    type = models.CharField(max_length=20)
    description2_txt = models.CharField(max_length=60)
    wkb_geometry = models.PointField()

    class Meta:
        managed = False
        db_table = 'POI_view'

class DisasterNeighborhoodView(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    wkb_geometry = models.GeometryField()
    pgd_landslide_dry_mean_di = models.CharField(max_length=50)
    pgd_total_wet_mean_di = models.CharField(max_length=50) ###
    pgv_site_mean_mmi_txt = models.CharField(max_length=10) ###
    pgv_site_mean_desc = models.CharField(max_length=255)
    census_response_rate = models.FloatField()

    class Meta:
        managed = False
        db_table = 'disaster_neighborhood_view'


CHLOROPLETHMAP = 'CM'
SCATTERPLOTMAP = 'SM'
PATHMAP = 'PM'
POLYGONPLOTMAP = 'PP'
ICONMAP = 'IM'
SCREENGRIDMAP = 'SG'

VISUALIZATION_CHOICES = (
    (CHLOROPLETHMAP, 'ChoroplethMap'),
    (SCATTERPLOTMAP, 'ScatterPlotMap'),
    (PATHMAP, 'PathMap'),
    (POLYGONPLOTMAP, 'PolygonPlotMap'),
    (ICONMAP, 'IconMap'),
    (SCREENGRIDMAP, 'ScreenGridMap'),
)

class Slide(models.Model):
    name = models.CharField(max_length=80)
    endpoint = models.URLField()
    visualization = models.CharField(max_length=2, choices=VISUALIZATION_CHOICES, default=SCATTERPLOTMAP)

    def __str__(self):
        return self.name

class Foundation(models.Model):
    name = models.CharField(max_length=80)
    endpoint = models.URLField()
    visualization = models.CharField(max_length=2, choices=VISUALIZATION_CHOICES, default=SCATTERPLOTMAP)

    def __str__(self):
        return self.name

class Packages(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=200)
    foundations = models.ManyToManyField(Foundation, related_name='foundations', related_query_name='foundation')
    default_foundation = models.ForeignKey(Foundation, on_delete=models.SET_NULL, null=True, related_name='default_foundation')
    slides = models.ManyToManyField(Slide, related_name='slides', related_query_name='slide')
    default_slide = models.ForeignKey(Slide, on_delete=models.SET_NULL, null=True, related_name='default_slide')

    def __str__(self):
        return self.name
