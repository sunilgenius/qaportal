# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-10 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180710_2047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pwa',
            name='sizes',
        ),
        migrations.RemoveField(
            model_name='pwa',
            name='type_of_icon',
        ),
        migrations.AddField(
            model_name='pwa',
            name='background_color',
            field=models.CharField(default='#3E4EB8', max_length=200),
        ),
        migrations.AddField(
            model_name='pwa',
            name='display',
            field=models.CharField(default='standalon', max_length=200),
        ),
        migrations.AddField(
            model_name='pwa',
            name='icon_src_2',
            field=models.CharField(default='add link to image', max_length=200),
        ),
        migrations.AddField(
            model_name='pwa',
            name='icon_src_3',
            field=models.CharField(default='add link to image', max_length=200),
        ),
        migrations.AddField(
            model_name='pwa',
            name='icon_src_4',
            field=models.CharField(default='add link to image', max_length=200),
        ),
        migrations.AddField(
            model_name='pwa',
            name='icon_src_5',
            field=models.CharField(default='add link to image', max_length=200),
        ),
        migrations.AddField(
            model_name='pwa',
            name='icon_src_6',
            field=models.CharField(default='add link to image', max_length=200),
        ),
        migrations.AddField(
            model_name='pwa',
            name='size_1',
            field=models.CharField(default='128x128', max_length=200),
        ),
        migrations.AddField(
            model_name='pwa',
            name='size_2',
            field=models.CharField(default='144x144', max_length=200),
        ),
        migrations.AddField(
            model_name='pwa',
            name='size_3',
            field=models.CharField(default='152x152', max_length=200),
        ),
        migrations.AddField(
            model_name='pwa',
            name='size_4',
            field=models.CharField(default='192x192', max_length=200),
        ),
        migrations.AddField(
            model_name='pwa',
            name='size_5',
            field=models.CharField(default='256x256', max_length=200),
        ),
        migrations.AddField(
            model_name='pwa',
            name='size_6',
            field=models.CharField(default='512x512', max_length=200),
        ),
        migrations.AddField(
            model_name='pwa',
            name='theme_color',
            field=models.CharField(default='#2F3BA2', max_length=200),
        ),
        migrations.AddField(
            model_name='pwa',
            name='type_of_icon_1',
            field=models.CharField(default='image/png', max_length=200),
        ),
        migrations.AddField(
            model_name='pwa',
            name='type_of_icon_2',
            field=models.CharField(default='image/png', max_length=200),
        ),
        migrations.AddField(
            model_name='pwa',
            name='type_of_icon_3',
            field=models.CharField(default='image/png', max_length=200),
        ),
        migrations.AddField(
            model_name='pwa',
            name='type_of_icon_4',
            field=models.CharField(default='image/png', max_length=200),
        ),
        migrations.AddField(
            model_name='pwa',
            name='type_of_icon_5',
            field=models.CharField(default='image/png', max_length=200),
        ),
        migrations.AddField(
            model_name='pwa',
            name='type_of_icon_6',
            field=models.CharField(default='image/png', max_length=200),
        ),
        migrations.AlterField(
            model_name='pwa',
            name='icon_src_1',
            field=models.CharField(default='add link to image', max_length=200),
        ),
        migrations.AlterField(
            model_name='pwa',
            name='start_url',
            field=models.CharField(default='/', max_length=200),
        ),
    ]
