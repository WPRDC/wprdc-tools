# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-15 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geostuff', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blockgroup',
            name='geo_id',
        ),
        migrations.AddField(
            model_name='blockgroup',
            name='fid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]