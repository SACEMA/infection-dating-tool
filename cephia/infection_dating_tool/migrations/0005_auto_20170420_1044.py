# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-04-20 08:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infection_dating_tool', '0004_auto_20170209_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idtfileinfo',
            name='data_file',
            field=models.FileField(upload_to='/home/andrew/id/idt_prod/cephia/cephia/../../media/infection_dating_tool_uploads'),
        ),
    ]
