from django.db import models

# Create your models here.
from scenic.models import Scenic
from user.models import User


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    scenic = models.ForeignKey(Scenic, models.DO_NOTHING, blank=True, null=True)
    time = models.DateTimeField()
    mark = models.IntegerField()
    content = models.CharField(max_length=1024)
    clap = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment'


class ComImg(models.Model):
    com_img_id = models.AutoField(primary_key=True)
    comment = models.ForeignKey('Comment', models.DO_NOTHING, blank=True, null=True)
    img_url = models.CharField(max_length=512)

    class Meta:
        managed = False
        db_table = 'com_img'
