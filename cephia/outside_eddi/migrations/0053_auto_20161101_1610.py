# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-01 14:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outside_eddi', '0052_auto_20161101_1609'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='outsideeddisubject',
            unique_together=set([('subject_label', 'user')]),
        ),
    ]