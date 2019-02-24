from django.db import models

# Create your models here.
from map.models import Region


class SceImg(models.Model):
    sce_img_id = models.AutoField(primary_key=True)
    scenic = models.ForeignKey('Scenic', models.DO_NOTHING, verbose_name='景点')
    img_url = models.CharField(max_length=512, verbose_name='景点图片')

    class Meta:
        # managed = False
        db_table = 'sce_img'


class Scenic(models.Model):
    scenic_id = models.AutoField(primary_key=True)
    region = models.ForeignKey(Region, models.DO_NOTHING, blank=True, null=True, verbose_name='区')
    name = models.CharField(max_length=512, verbose_name='景点名')
    abstract = models.CharField(max_length=4096, verbose_name='景点简述')
    detail = models.TextField(blank=True, null=True, verbose_name='景点详细描述')
    addr = models.CharField(max_length=512, verbose_name='景点地址')
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, verbose_name='经度')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, verbose_name='纬度')
    cover = models.CharField(max_length=512, blank=True, null=True, verbose_name='封面图')
    ticket = models.CharField(max_length=512, blank=True, null=True, verbose_name='门票')
    trans = models.CharField(max_length=512, blank=True, null=True, verbose_name='交通')
    open_time = models.CharField(max_length=512, blank=True, null=True, verbose_name='开放时间')
    recommend_time = models.CharField(max_length=512, blank=True, null=True, verbose_name='推荐游玩时间')
    tel = models.CharField(max_length=50, blank=True, null=True, verbose_name='电话号码')

    # 景点系统推荐热度，用下面爬虫抓的数据算
    hot_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, verbose_name='热度')

    class Meta:
        # managed = False
        db_table = 'scenic'


# 爬虫抓取的该景点点评数，注意，是爬虫抓取的，用来算系统推荐的景点的热度
class Sce_spider_comment(models.Model):
    sce_spider_comment_id = models.AutoField(primary_key=True)
    scenic = models.ForeignKey('Scenic', models.DO_NOTHING, verbose_name='景点')
    total_nums = models.IntegerField(default=0, verbose_name='点评总数')
    good_nums = models.IntegerField(default=0, verbose_name='好评数')

    class Meta:
        # managed = False
        db_table = 'sce_spider_comment'
