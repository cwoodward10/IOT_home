# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-26 22:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sensorsHome', '0020_auto_20170204_2244'),
    ]

    operations = [
        migrations.CreateModel(
            name='TSl251_readings',
            fields=[
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, primary_key=True, serialize=False, unique=True, verbose_name=b'date and time of reading')),
                ('lux', models.FloatField(default=-1000)),
                ('TSL2561', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensorsHome.Sensor')),
            ],
        ),
    ]
