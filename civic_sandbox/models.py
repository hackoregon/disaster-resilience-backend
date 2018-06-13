from django.contrib.gis.db import models

class POI(models.Model): 
    pk_id= models.CharField(primary_key=True, max_length=30,)
    type = models.CharField(max_length=20)
    description2_txt = models.CharField(max_length=60)
    wkb_geometry = models.PointField()

    class Meta:
        managed = False
        db_table = 'POI_view'
