# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-21 09:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import lib.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('outside_eddi', '0026_auto_20161021_1112'),
    ]

    operations = [
        migrations.CreateModel(
            name='EDDITable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('dates', models.DateField(null=True)),
                ('results', models.CharField(max_length=15, null=True)),
                ('test_file', lib.fields.ProtectedForeignKey(on_delete=django.db.models.deletion.PROTECT, to='outside_eddi.TestHistoryFile')),
                ('user', lib.fields.ProtectedForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]