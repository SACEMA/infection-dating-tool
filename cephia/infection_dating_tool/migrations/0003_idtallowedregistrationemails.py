# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-09 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infection_dating_tool', '0002_idtsubject_flag'),
    ]

    operations = [
        migrations.CreateModel(
            name='IDTAllowedRegistrationEmails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'idt_allowed_registration_emails',
            },
        ),
    ]