# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from map.models import City
from scenic.models import Scenic


class Circle(models.Model):
    circle_id = models.AutoField(primary_key=True)
    city = models.ForeignKey(City, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=128)
    level = models.IntegerField()
    avatar = models.CharField(max_length=512, blank=True, null=True)
    abstract = models.CharField(max_length=512, blank=True, null=True)
    user_nums = models.IntegerField()
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'circle'


class CircleRec(models.Model):
    circle_rec_id = models.AutoField(primary_key=True)
    scenic = models.ForeignKey(Scenic, models.DO_NOTHING, blank=True, null=True)
    circle = models.ForeignKey(Circle, models.DO_NOTHING, blank=True, null=True)
    rec_nums = models.IntegerField()
    month = models.DateField()

    class Meta:
        # managed = False
        db_table = 'circle_rec'

