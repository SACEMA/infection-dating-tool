# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-14 10:21
from __future__ import unicode_literals

import cephia.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cephia', '0070_fix_visit_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='assay',
            name='created_by',
            field=cephia.fields.ProtectedForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='assays', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='assay',
            name='is_custom',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='fileinfo',
            name='data_file',
            field=models.FileField(upload_to=b'/home/keith/id/cephia/cephia/cephia/../../media'),
        ),
    ]
