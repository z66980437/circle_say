# Generated by Django 2.1.7 on 2019-02-23 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='time',
        ),
        migrations.AddField(
            model_name='comment',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='评论时间'),
        ),
        migrations.AlterField(
            model_name='comimg',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='comment.Comment', verbose_name='评论'),
        ),
        migrations.AlterField(
            model_name='comimg',
            name='img_url',
            field=models.CharField(max_length=512, verbose_name='评论图片'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='clap',
            field=models.IntegerField(blank=True, null=True, verbose_name='对该评论的点赞数'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(max_length=1024, verbose_name='评论内容'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='mark',
            field=models.IntegerField(verbose_name='对景点的评分'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='scenic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='scenic.Scenic', verbose_name='景点'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.User', verbose_name='用户'),
        ),
    ]
