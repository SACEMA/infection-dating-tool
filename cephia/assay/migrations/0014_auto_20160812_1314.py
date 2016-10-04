# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-12 11:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cephia', '0056_auto_20160810_1509'),
        ('assay', '0013_auto_20160810_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='assayrun',
            name='contains_all_panel_visits',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='assayrun',
            name='contains_visits_outside_panel',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='assayrun',
            name='has_expected_num_replicates',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='assayrun',
            name='visits_missing_from_panel',
            field=models.ManyToManyField(related_name='assay_run_missing_visits', to='cephia.Visit'),
        ),
        migrations.AddField(
            model_name='assayrun',
            name='visits_not_in_panel',
            field=models.ManyToManyField(related_name='assay_run_extra_visits', to='cephia.Visit'),
        ),
        migrations.AlterField(
            model_name='panelmembership',
            name='panel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='cephia.Panel'),
        ),
        migrations.AlterField(
            model_name='panelmembership',
            name='visit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='visits', to='cephia.Visit'),
        ),
    ]