# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-29 09:46
from __future__ import unicode_literals

import cephia.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cephia', '0058_auto_20160829_1056'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViralLoadRow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[(b'recalled', b'Recalled'), (b'pending', b'Pending'), (b'validated', b'Validated'), (b'imported', b'Imported'), (b'processed', b'Processed'), (b'error', b'Error')], max_length=10)),
                ('error_message', models.TextField(blank=True)),
                ('date_processed', models.DateTimeField(auto_now_add=True)),
                ('specimen_label', models.CharField(max_length=255, null=True)),
                ('relation', models.CharField(max_length=255, null=True)),
                ('viral_load', models.CharField(max_length=255, null=True)),
                ('comment', models.CharField(max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='fileinfo',
            name='file_type',
            field=models.CharField(choices=[(b'', b'---------'), (b'aliquot', b'Aliquot'), (b'assay', b'Assay'), (b'diagnostic_test', b'Diagnostic Test'), (b'panel_shipment', b'Panel Shipment'), (b'panel_membership', b'Panel Membership'), (b'protocol_lookup', b'Protocol Lookup'), (b'subject', b'Subject'), (b'test_history', b'Diagnostic Test History'), (b'test_property', b'Diagnostic Test Properties'), (b'transfer_in', b'Transfer In'), (b'transfer_out', b'Transfer Out'), (b'visit', b'Visit'), (b'viral_load', b'Viral Load')], max_length=20),
        ),
        migrations.AlterField(
            model_name='historicalfileinfo',
            name='file_type',
            field=models.CharField(choices=[(b'', b'---------'), (b'aliquot', b'Aliquot'), (b'assay', b'Assay'), (b'diagnostic_test', b'Diagnostic Test'), (b'panel_shipment', b'Panel Shipment'), (b'panel_membership', b'Panel Membership'), (b'protocol_lookup', b'Protocol Lookup'), (b'subject', b'Subject'), (b'test_history', b'Diagnostic Test History'), (b'test_property', b'Diagnostic Test Properties'), (b'transfer_in', b'Transfer In'), (b'transfer_out', b'Transfer Out'), (b'visit', b'Visit'), (b'viral_load', b'Viral Load')], max_length=20),
        ),
        migrations.AddField(
            model_name='viralloadrow',
            name='fileinfo',
            field=cephia.fields.ProtectedForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cephia.FileInfo'),
        ),
    ]
