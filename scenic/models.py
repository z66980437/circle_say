from django.db import models

# Create your models here.
from map.models import Region


class SceImg(models.Model):
    sce_img_id = models.AutoField(primary_key=True)
    scenic = models.ForeignKey('Scenic', models.DO_NOTHING)
    img_url = models.CharField(max_length=512)

    class Meta:
        # managed = False
        db_table = 'sce_img'


class Scenic(models.Model):
    scenic_id = models.AutoField(primary_key=True)
    region = models.ForeignKey(Region, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=512)
    abstract = models.CharField(max_length=4096)
    detail = models.TextField(blank=True, null=True)
    addr = models.CharField(max_length=512)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    cover = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'scenic'
