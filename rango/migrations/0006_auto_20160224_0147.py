# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-24 01:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_auto_20160218_0724'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='first_visit',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 24, 1, 47, 48, 114402)),
        ),
        migrations.AddField(
            model_name='page',
            name='last_visit',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 24, 1, 47, 48, 114438)),
        ),
    ]