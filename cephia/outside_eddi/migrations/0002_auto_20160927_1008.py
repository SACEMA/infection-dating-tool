# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-27 08:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outside_eddi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testhistoryfile',
            old_name='test_history_file',
            new_name='data_file',
        ),
    ]
