from django.db import models

# Create your models here.


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    province = models.ForeignKey('Province', models.DO_NOTHING, blank=True, null=True, verbose_name='省')
    name = models.CharField(max_length=128, verbose_name='市名')
    sce_nums = models.IntegerField(default=0, verbose_name='景点数目')

    class Meta:
        # managed = False
        db_table = 'city'


class Province(models.Model):
    province_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, verbose_name='省名')
    sce_nums = models.IntegerField(default=0, verbose_name='景点数目')

    class Meta:
        # managed = False
        db_table = 'province'


class Region(models.Model):
    region_id = models.AutoField(primary_key=True)
    city = models.ForeignKey(City, models.DO_NOTHING, blank=True, null=True, verbose_name='市')
    name = models.CharField(max_length=128, verbose_name='区名')
    sce_nums = models.IntegerField(default=0, verbose_name='景点数目')

    class Meta:
        # managed = False
        db_table = 'region'
