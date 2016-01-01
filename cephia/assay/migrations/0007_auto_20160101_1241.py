# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cephia', '0016_auto_20160101_1241'),
        ('assay', '0006_panelmembershiprow_panelshipmentrow'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchitectResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('specimen', models.CharField(max_length=255, blank=True)),
                ('assay', models.CharField(max_length=255, blank=True)),
                ('sample_type', models.CharField(max_length=255, blank=True)),
                ('site', models.CharField(max_length=255, blank=True)),
                ('test_date', models.CharField(max_length=255, blank=True)),
                ('operator', models.CharField(max_length=255, blank=True)),
                ('assay_kit_lot_id', models.CharField(max_length=255, blank=True)),
                ('plate_id', models.CharField(max_length=255, blank=True)),
                ('test_mode', models.CharField(max_length=255, blank=True)),
                ('well', models.CharField(max_length=255, blank=True)),
                ('intermediate_1', models.CharField(max_length=255, blank=True)),
                ('intermediate_2', models.CharField(max_length=255, blank=True)),
                ('intermediate_3', models.CharField(max_length=255, blank=True)),
                ('intermediate_4', models.CharField(max_length=255, blank=True)),
                ('intermediate_5', models.CharField(max_length=255, blank=True)),
                ('intermediate_6', models.CharField(max_length=255, blank=True)),
                ('final_result', models.CharField(max_length=255, blank=True)),
                ('panel_type', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'db_table': 'architect_result',
            },
        ),
        migrations.CreateModel(
            name='ArchitectResultRow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(max_length=10, choices=[(b'pending', b'Pending'), (b'validated', b'Validated'), (b'imported', b'Imported'), (b'processed', b'Processed'), (b'error', b'Error')])),
                ('error_message', models.TextField(blank=True)),
                ('date_processed', models.DateTimeField(auto_now_add=True)),
                ('specimen', models.CharField(max_length=255, blank=True)),
                ('assay', models.CharField(max_length=255, blank=True)),
                ('sample_type', models.CharField(max_length=255, blank=True)),
                ('site', models.CharField(max_length=255, blank=True)),
                ('test_date', models.CharField(max_length=255, blank=True)),
                ('operator', models.CharField(max_length=255, blank=True)),
                ('assay_kit_lot_id', models.CharField(max_length=255, blank=True)),
                ('plate_id', models.CharField(max_length=255, blank=True)),
                ('test_mode', models.CharField(max_length=255, blank=True)),
                ('well', models.CharField(max_length=255, blank=True)),
                ('intermediate_1', models.CharField(max_length=255, blank=True)),
                ('intermediate_2', models.CharField(max_length=255, blank=True)),
                ('intermediate_3', models.CharField(max_length=255, blank=True)),
                ('intermediate_4', models.CharField(max_length=255, blank=True)),
                ('intermediate_5', models.CharField(max_length=255, blank=True)),
                ('intermediate_6', models.CharField(max_length=255, blank=True)),
                ('final_result', models.CharField(max_length=255, blank=True)),
                ('panel_type', models.CharField(max_length=255, blank=True)),
                ('fileinfo', models.ForeignKey(to='cephia.FileInfo')),
            ],
            options={
                'db_table': 'architect_result_row',
            },
        ),
        migrations.CreateModel(
            name='BioradResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('specimen', models.CharField(max_length=255, blank=True)),
                ('assay', models.CharField(max_length=255, blank=True)),
                ('sample_type', models.CharField(max_length=255, blank=True)),
                ('site', models.CharField(max_length=255, blank=True)),
                ('test_date', models.CharField(max_length=255, blank=True)),
                ('operator', models.CharField(max_length=255, blank=True)),
                ('assay_kit_lot_id', models.CharField(max_length=255, blank=True)),
                ('plate_id', models.CharField(max_length=255, blank=True)),
                ('test_mode', models.CharField(max_length=255, blank=True)),
                ('well', models.CharField(max_length=255, blank=True)),
                ('intermediate_1', models.CharField(max_length=255, blank=True)),
                ('intermediate_2', models.CharField(max_length=255, blank=True)),
                ('intermediate_3', models.CharField(max_length=255, blank=True)),
                ('intermediate_4', models.CharField(max_length=255, blank=True)),
                ('intermediate_5', models.CharField(max_length=255, blank=True)),
                ('intermediate_6', models.CharField(max_length=255, blank=True)),
                ('final_result', models.CharField(max_length=255, blank=True)),
                ('panel_type', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'db_table': 'biorad_result',
            },
        ),
        migrations.CreateModel(
            name='BioradResultRow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(max_length=10, choices=[(b'pending', b'Pending'), (b'validated', b'Validated'), (b'imported', b'Imported'), (b'processed', b'Processed'), (b'error', b'Error')])),
                ('error_message', models.TextField(blank=True)),
                ('date_processed', models.DateTimeField(auto_now_add=True)),
                ('specimen', models.CharField(max_length=255, blank=True)),
                ('assay', models.CharField(max_length=255, blank=True)),
                ('sample_type', models.CharField(max_length=255, blank=True)),
                ('site', models.CharField(max_length=255, blank=True)),
                ('test_date', models.CharField(max_length=255, blank=True)),
                ('operator', models.CharField(max_length=255, blank=True)),
                ('assay_kit_lot_id', models.CharField(max_length=255, blank=True)),
                ('plate_id', models.CharField(max_length=255, blank=True)),
                ('test_mode', models.CharField(max_length=255, blank=True)),
                ('well', models.CharField(max_length=255, blank=True)),
                ('intermediate_1', models.CharField(max_length=255, blank=True)),
                ('intermediate_2', models.CharField(max_length=255, blank=True)),
                ('intermediate_3', models.CharField(max_length=255, blank=True)),
                ('intermediate_4', models.CharField(max_length=255, blank=True)),
                ('intermediate_5', models.CharField(max_length=255, blank=True)),
                ('intermediate_6', models.CharField(max_length=255, blank=True)),
                ('final_result', models.CharField(max_length=255, blank=True)),
                ('panel_type', models.CharField(max_length=255, blank=True)),
                ('fileinfo', models.ForeignKey(to='cephia.FileInfo')),
            ],
            options={
                'db_table': 'biorad_result_row',
            },
        ),
        migrations.CreateModel(
            name='LagResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('specimen', models.CharField(max_length=255, blank=True)),
                ('assay', models.CharField(max_length=255, blank=True)),
                ('sample_type', models.CharField(max_length=255, blank=True)),
                ('site', models.CharField(max_length=255, blank=True)),
                ('test_date', models.CharField(max_length=255, blank=True)),
                ('operator', models.CharField(max_length=255, blank=True)),
                ('assay_kit_lot_id', models.CharField(max_length=255, blank=True)),
                ('plate_id', models.CharField(max_length=255, blank=True)),
                ('test_mode', models.CharField(max_length=255, blank=True)),
                ('well', models.CharField(max_length=255, blank=True)),
                ('intermediate_1', models.CharField(max_length=255, blank=True)),
                ('intermediate_2', models.CharField(max_length=255, blank=True)),
                ('intermediate_3', models.CharField(max_length=255, blank=True)),
                ('intermediate_4', models.CharField(max_length=255, blank=True)),
                ('intermediate_5', models.CharField(max_length=255, blank=True)),
                ('intermediate_6', models.CharField(max_length=255, blank=True)),
                ('final_result', models.CharField(max_length=255, blank=True)),
                ('panel_type', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'db_table': 'lag_result',
            },
        ),
        migrations.CreateModel(
            name='LagResultRow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(max_length=10, choices=[(b'pending', b'Pending'), (b'validated', b'Validated'), (b'imported', b'Imported'), (b'processed', b'Processed'), (b'error', b'Error')])),
                ('error_message', models.TextField(blank=True)),
                ('date_processed', models.DateTimeField(auto_now_add=True)),
                ('specimen', models.CharField(max_length=255, blank=True)),
                ('assay', models.CharField(max_length=255, blank=True)),
                ('sample_type', models.CharField(max_length=255, blank=True)),
                ('site', models.CharField(max_length=255, blank=True)),
                ('test_date', models.CharField(max_length=255, blank=True)),
                ('operator', models.CharField(max_length=255, blank=True)),
                ('assay_kit_lot_id', models.CharField(max_length=255, blank=True)),
                ('plate_id', models.CharField(max_length=255, blank=True)),
                ('test_mode', models.CharField(max_length=255, blank=True)),
                ('well', models.CharField(max_length=255, blank=True)),
                ('intermediate_1', models.CharField(max_length=255, blank=True)),
                ('intermediate_2', models.CharField(max_length=255, blank=True)),
                ('intermediate_3', models.CharField(max_length=255, blank=True)),
                ('intermediate_4', models.CharField(max_length=255, blank=True)),
                ('intermediate_5', models.CharField(max_length=255, blank=True)),
                ('intermediate_6', models.CharField(max_length=255, blank=True)),
                ('final_result', models.CharField(max_length=255, blank=True)),
                ('panel_type', models.CharField(max_length=255, blank=True)),
                ('fileinfo', models.ForeignKey(to='cephia.FileInfo')),
            ],
            options={
                'db_table': 'lag_result_row',
            },
        ),
        migrations.CreateModel(
            name='VitrosResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('specimen', models.CharField(max_length=255, blank=True)),
                ('assay', models.CharField(max_length=255, blank=True)),
                ('sample_type', models.CharField(max_length=255, blank=True)),
                ('site', models.CharField(max_length=255, blank=True)),
                ('test_date', models.CharField(max_length=255, blank=True)),
                ('operator', models.CharField(max_length=255, blank=True)),
                ('assay_kit_lot_id', models.CharField(max_length=255, blank=True)),
                ('plate_id', models.CharField(max_length=255, blank=True)),
                ('test_mode', models.CharField(max_length=255, blank=True)),
                ('well', models.CharField(max_length=255, blank=True)),
                ('intermediate_1', models.CharField(max_length=255, blank=True)),
                ('intermediate_2', models.CharField(max_length=255, blank=True)),
                ('intermediate_3', models.CharField(max_length=255, blank=True)),
                ('intermediate_4', models.CharField(max_length=255, blank=True)),
                ('intermediate_5', models.CharField(max_length=255, blank=True)),
                ('intermediate_6', models.CharField(max_length=255, blank=True)),
                ('final_result', models.CharField(max_length=255, blank=True)),
                ('panel_type', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'db_table': 'vitros_result',
            },
        ),
        migrations.CreateModel(
            name='VitrosResultRow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(max_length=10, choices=[(b'pending', b'Pending'), (b'validated', b'Validated'), (b'imported', b'Imported'), (b'processed', b'Processed'), (b'error', b'Error')])),
                ('error_message', models.TextField(blank=True)),
                ('date_processed', models.DateTimeField(auto_now_add=True)),
                ('specimen', models.CharField(max_length=255, blank=True)),
                ('assay', models.CharField(max_length=255, blank=True)),
                ('sample_type', models.CharField(max_length=255, blank=True)),
                ('site', models.CharField(max_length=255, blank=True)),
                ('test_date', models.CharField(max_length=255, blank=True)),
                ('operator', models.CharField(max_length=255, blank=True)),
                ('assay_kit_lot_id', models.CharField(max_length=255, blank=True)),
                ('plate_id', models.CharField(max_length=255, blank=True)),
                ('test_mode', models.CharField(max_length=255, blank=True)),
                ('well', models.CharField(max_length=255, blank=True)),
                ('intermediate_1', models.CharField(max_length=255, blank=True)),
                ('intermediate_2', models.CharField(max_length=255, blank=True)),
                ('intermediate_3', models.CharField(max_length=255, blank=True)),
                ('intermediate_4', models.CharField(max_length=255, blank=True)),
                ('intermediate_5', models.CharField(max_length=255, blank=True)),
                ('intermediate_6', models.CharField(max_length=255, blank=True)),
                ('final_result', models.CharField(max_length=255, blank=True)),
                ('panel_type', models.CharField(max_length=255, blank=True)),
                ('fileinfo', models.ForeignKey(to='cephia.FileInfo')),
            ],
            options={
                'db_table': 'vitros_result_row',
            },
        ),
        migrations.DeleteModel(
            name='Assay',
        ),
    ]
