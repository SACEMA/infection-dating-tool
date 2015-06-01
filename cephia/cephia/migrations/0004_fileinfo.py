# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cephia', '0003_auto_20150601_0935'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('filename', models.FileField(upload_to=b'file_archive')),
                ('state', models.CharField(max_length=20, choices=[(b'pending', b'Pending'), (b'imported', b'Imported'), (b'error', b'Error')])),
                ('message', models.TextField(null=True)),
                ('file_type', models.CharField(max_length=20, choices=[(b'test', b'Test File')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'cephia_fileinfo',
            },
        ),
    ]
