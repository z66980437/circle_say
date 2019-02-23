from django.db import models

# Create your models here.
from scenic.models import Scenic
from user.models import User


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, verbose_name='用户')
    scenic = models.ForeignKey(Scenic, models.DO_NOTHING, blank=True, null=True, verbose_name='景点')
    add_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='评论时间')
    mark = models.IntegerField(verbose_name='对景点的评分')
    content = models.CharField(max_length=1024, verbose_name='评论内容')
    clap = models.IntegerField(blank=True, null=True, verbose_name='对该评论的点赞数')

    class Meta:
        # managed = False
        db_table = 'comment'


class ComImg(models.Model):
    com_img_id = models.AutoField(primary_key=True)
    comment = models.ForeignKey('Comment', models.DO_NOTHING, blank=True, null=True, verbose_name='评论')
    img_url = models.CharField(max_length=512, verbose_name='评论图片')

    class Meta:
        # managed = False
        db_table = 'com_img'
