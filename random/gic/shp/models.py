from django.db import models
from django.contrib.gis.db import models as gis_models

# Create your models here.
class NepalDistrict(models.Model):
    ddgn = models.AutoField(db_column='DDGN', primary_key=True)  # Field name made lowercase.
    geom = gis_models.MultiPolygonField(blank=True, null=True)
    ddgn_0 = models.BigIntegerField(db_column='ddgn', blank=True, null=True)  # Field renamed because of name conflict.
    first_dcod = models.BigIntegerField(blank=True, null=True)
    first_dist = models.CharField(max_length=50, blank=True, null=True)
    first_gn_c = models.FloatField(blank=True, null=True)
    first_stat = models.BigIntegerField(blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    centroid_x = models.FloatField(blank=True, null=True)
    centroid_y = models.FloatField(blank=True, null=True)
    
    # def me(self):
    #     return self.shape_area

    class Meta:
        managed = False
        db_table = 'nepal_district'
    # def __str__(self):
    #     return self.first_dist
