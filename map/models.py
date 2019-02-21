from django.db import models

# Create your models here.


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    province = models.ForeignKey('Province', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=128)
    sce_nums = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'city'


class Province(models.Model):
    province_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    sce_nums = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'province'


class Region(models.Model):
    region_id = models.AutoField(primary_key=True)
    city = models.ForeignKey(City, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=128)
    sce_nums = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'region'
