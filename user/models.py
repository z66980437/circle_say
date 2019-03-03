from django.db import models

# Create your models here.
from circle.models import Circle
from map.models import Region
from scenic.models import Scenic


class Relation(models.Model):
    relation_id = models.AutoField(primary_key=True, db_column='pk')
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=False, verbose_name='用户', related_name='user')
    friend = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=False, verbose_name='朋友', related_name='friend')
    add_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='添加时间')
    is_show = models.IntegerField(blank=True, null=True, verbose_name='是否对其展示足迹')
    is_delete = models.IntegerField(blank=True, null=True, verbose_name='黑名单等操作相关')

    class Meta:
        # managed = False
        db_table = 'friends'


class LoginLog(models.Model):
    """登录日志"""

    logid = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.DO_NOTHING, db_column='userid')
    ipaddr = models.CharField(max_length=255)
    logdate = models.DateTimeField(auto_now_add=True)
    devcode = models.CharField(max_length=255, default='', null=True)

    class Meta:
        # managed = False
        db_table = 'login_log'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    region = models.ForeignKey(Region, models.DO_NOTHING, blank=True, null=True, verbose_name='区')
    username = models.CharField(max_length=16, verbose_name='用户账号')
    password = models.CharField(max_length=512, verbose_name='密码')
    nickname = models.CharField(max_length=16, verbose_name='昵称')
    real_name = models.CharField(max_length=16, blank=True, null=True, verbose_name='真实姓名')
    age = models.IntegerField(blank=True, null=True, verbose_name='活了多久')
    gender = models.IntegerField(blank=True, null=True, verbose_name='性别')
    card_id = models.CharField(max_length=18, blank=True, null=True, verbose_name='身份证号')
    tel = models.CharField(max_length=16, blank=True, null=True, verbose_name='电话号码')
    email = models.CharField(max_length=32, blank=True, null=True, verbose_name='邮箱')
    avatar = models.CharField(max_length=512, blank=True, null=True, verbose_name='头像')
    signature = models.CharField(max_length=256, blank=True, null=True, verbose_name='个性签名')
    is_delete = models.IntegerField(blank=True, null=True, verbose_name='是否删除')
    lastvisit = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    circles = models.ManyToManyField(Circle, through='UserCircle', verbose_name='所加的圈子')
    # friends = models.ManyToManyField('self', through='Relation')

    class Meta:
        # managed = False
        db_table = 'users'


class UserCircle(models.Model):
    circle = models.ForeignKey(Circle, models.DO_NOTHING, verbose_name='圈子')
    user = models.ForeignKey(User, models.DO_NOTHING, verbose_name='用户')
    privg = models.IntegerField(default=0, verbose_name="权限，0：圈主，1：管理员， 2：群众")

    class Meta:
        # managed = False
        db_table = 'user_circle'
        unique_together = ('circle', 'user')

class UserRec(models.Model):
    user_rec_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, verbose_name='用户')
    scenic = models.ForeignKey(Scenic, models.DO_NOTHING, blank=True, null=True, verbose_name='景点')
    rec_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='打卡时间')

    class Meta:
        # managed = False
        db_table = 'user_rec'
