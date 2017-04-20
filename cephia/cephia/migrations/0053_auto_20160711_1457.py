# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-11 12:57
from __future__ import unicode_literals

from django.db import migrations


from django.contrib.auth.management import create_permissions

def add_permissions(apps, schema_editor):
    apps.models_module = True
    create_permissions(apps)
    apps.models_module = None

class Migration(migrations.Migration):

    dependencies = [
        ('cephia', '0052_auto_20160706_1554'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cephiauser',
            options={'permissions': [('can_upload_panel_data', 'Can upload memberships and shipments'), ('can_upload_results', 'Can upload results'), ('can_upload_clinical_data', 'Can upload subjects and visits'), ('can_upload_eddi_data', 'Can upload diagnostic data'), ('can_upload_specimen_data', 'Can upload aliquot, transfer in, transfer out')]},
        ),
        migrations.RunPython(add_permissions, migrations.RunPython.noop)
    ]
