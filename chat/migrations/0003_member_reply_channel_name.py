# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-19 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20160819_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='reply_channel_name',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]
