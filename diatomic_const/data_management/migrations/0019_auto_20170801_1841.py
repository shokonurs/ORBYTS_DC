# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-01 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_management', '0018_auto_20170801_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='molecular_state',
            name='projected_angular_momentum',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2),
        ),
        migrations.AlterField(
            model_name='molecular_state',
            name='total_angular_momentum',
            field=models.IntegerField(blank=True),
        ),
    ]
