# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-26 09:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import lib.fields


class Migration(migrations.Migration):

    dependencies = [
        ('outside_eddi', '0031_auto_20161025_1005'),
    ]

    operations = [
        migrations.CreateModel(
            name='OutsideEddiAssay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('long_name', models.CharField(max_length=255)),
                ('developer', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'outside_eddi_assay',
            },
        ),
        migrations.CreateModel(
            name='OutsideEddiCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'outside_eddi_countries',
            },
        ),
        migrations.CreateModel(
            name='OutsideEddiEthnicity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'outside_eddi_ethnicities',
            },
        ),
        migrations.CreateModel(
            name='OutsideEddiLaboratory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'outside_eddi_laboratories',
            },
        ),
        migrations.CreateModel(
            name='OutsideEddiLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'outside_eddi_locations',
            },
        ),
        migrations.CreateModel(
            name='OutsideEddiRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'outside_eddi_regions',
            },
        ),
        migrations.CreateModel(
            name='OutsideEddiSpecimenType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('spec_type', models.CharField(max_length=10)),
                ('spec_group', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'outside_eddi_specimen_types',
            },
        ),
        migrations.CreateModel(
            name='OutsideEddiStudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'outside_eddi_studies',
            },
        ),
        migrations.CreateModel(
            name='OutsideEddiSubtype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'outside_eddi_subtypes',
            },
        ),
        migrations.RemoveField(
            model_name='outsideeddidiagnostictesthistoryrow',
            name='fileinfo',
        ),
        migrations.RemoveField(
            model_name='outsideeddidiagnostictesthistoryrow',
            name='test_history',
        ),
        migrations.RemoveField(
            model_name='historicaloutsideeddidiagnostictesthistory',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='historicaloutsideeddidiagnostictesthistory',
            name='test',
        ),
        migrations.RemoveField(
            model_name='outsideeddidiagnostictesthistory',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='outsideeddidiagnostictesthistory',
            name='test',
        ),
        migrations.DeleteModel(
            name='OutsideEddiDiagnosticTestHistoryRow',
        ),
        migrations.AddField(
            model_name='outsideeddicountry',
            name='region',
            field=lib.fields.ProtectedForeignKey(on_delete=django.db.models.deletion.PROTECT, to='outside_eddi.OutsideEddiRegion'),
        ),
    ]