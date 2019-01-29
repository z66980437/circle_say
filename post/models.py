from django.db import models

# Create your models here.
from user.models import User


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    time = models.DateTimeField()
    abstract = models.CharField(max_length=128)
    content = models.TextField()
    score = models.IntegerField()
    clap = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post'


class PostComment(models.Model):
    post_com_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    content = models.TextField()
    time = models.DateTimeField()
    clap = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post_comment'
