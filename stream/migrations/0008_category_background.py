# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-05 04:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0007_auto_20160905_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='background',
            field=models.ImageField(default=None, upload_to='icons'),
            preserve_default=False,
        ),
    ]