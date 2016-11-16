# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-14 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outside_eddi', '0018_auto_20161013_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaloutsideedditestpropertyestimate',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicaloutsideedditestpropertyestimate',
            name='diagnostic_delay_median',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicaloutsideedditestpropertyestimate',
            name='name',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='historicaloutsideedditestpropertyestimate',
            name='variance',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='outsideedditestpropertyestimate',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='outsideedditestpropertyestimate',
            name='diagnostic_delay_median',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='outsideedditestpropertyestimate',
            name='name',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='outsideedditestpropertyestimate',
            name='variance',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]