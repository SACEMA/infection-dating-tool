# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-11-21 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infection_dating_tool', '0028_idtdiagnostictesthistory_diagnostic_delay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idtsubject',
            name='flag',
            field=models.CharField(max_length=300, null=True),
        ),
    ]