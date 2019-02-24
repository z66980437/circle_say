from django.db import models

# Create your models here.
from user.models import User


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, verbose_name='用户')
    release_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='发表时间')
    abstract = models.CharField(max_length=128, verbose_name='帖子摘要')
    content = models.TextField(verbose_name='内容')
    score = models.IntegerField(default=0)
    clap = models.IntegerField(blank=True, null=True, verbose_name='点赞数')

    class Meta:
        # managed = False
        db_table = 'post'


class PostComment(models.Model):
    post_com_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, models.DO_NOTHING, blank=True, null=True, verbose_name='帖子')
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, verbose_name='用户')
    content = models.TextField(verbose_name='内容')
    add_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='发表时间')
    clap = models.IntegerField(blank=True, null=True, verbose_name='对该回复点赞数')

    class Meta:
        # managed = False
        db_table = 'post_comment'
