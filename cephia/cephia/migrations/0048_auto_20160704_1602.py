# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-04 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cephia', '0047_auto_20160704_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalspecimen',
            name='is_artificicial',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='specimen',
            name='is_artificicial',
            field=models.BooleanField(default=False),
        ),
    ]
