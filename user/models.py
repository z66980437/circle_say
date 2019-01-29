from django.db import models

# Create your models here.
from circle.models import Circle
from map.models import Region
from scenic.models import Scenic


class Friends(models.Model):
    friends_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    add_time = models.DateTimeField()
    is_show = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'friends'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    region = models.ForeignKey(Region, models.DO_NOTHING, blank=True, null=True)
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=512)
    nickname = models.CharField(max_length=16)
    real_name = models.CharField(max_length=16, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    card_id = models.CharField(max_length=18, blank=True, null=True)
    tel = models.CharField(max_length=16, blank=True, null=True)
    email = models.CharField(max_length=32, blank=True, null=True)
    avatar = models.CharField(max_length=512, blank=True, null=True)
    signature = models.CharField(max_length=256, blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    circles = models.ManyToManyField(Circle, through='UserCircle')

    class Meta:
        managed = False
        db_table = 'user'


class UserCircle(models.Model):
    circle = models.ForeignKey(Circle, models.DO_NOTHING, primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_circle'
        unique_together = (('circle', 'user'),)


class UserRec(models.Model):
    user_rec_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    scenic = models.ForeignKey(Scenic, models.DO_NOTHING, blank=True, null=True)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_rec'
