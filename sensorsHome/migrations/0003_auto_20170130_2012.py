# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-31 02:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensorsHome', '0002_auto_20170130_1913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor',
            name='creation_date',
        ),
        migrations.AddField(
            model_name='dht11_readings',
            name='sensor_association',
            field=models.CharField(default='sensor', max_length=100),
        ),
        migrations.AddField(
            model_name='sensor',
            name='last_reading',
            field=models.DateTimeField(default='2012-09-04 06:00:00.000000-08:00', verbose_name='date and time of latest reading'),
        ),
    ]
