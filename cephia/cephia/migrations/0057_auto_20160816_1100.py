# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-16 09:00
from __future__ import unicode_literals

from django.db import migrations, models

visit_values = {}
historicalvisit_values = {}

def get_default_values(apps, schema):
    Visit = apps.get_model('cephia', 'Visit')
    HistoricalVisit = apps.get_model('cephia', 'HistoricalVisit')
    visit_values.update(Visit.objects.values_list('id', 'scopevisit_ec'))
    historicalvisit_values.update(HistoricalVisit.objects.values_list('id', 'scopevisit_ec'))
    Visit.objects.update(scopevisit_ec=None)
    HistoricalVisit.objects.update(scopevisit_ec=None)

def set_default_values(apps, schema):
    Visit = apps.get_model('cephia', 'Visit')
    HistoricalVisit = apps.get_model('cephia', 'HistoricalVisit')

    for k,v in visit_values.iteritems():
        if v == 'False':
            Visit.objects.filter(pk=k).update(scopevisit_ec=False)
        elif v == 'True':
            Visit.objects.filter(pk=k).update(scopevisit_ec=True)

    for k,v in historicalvisit_values.iteritems():
        if v == 'False':
            HistoricalVisit.objects.filter(pk=k).update(scopevisit_ec=False)
        elif v == 'True':
            HistoricalVisit.objects.filter(pk=k).update(scopevisit_ec=True)


class Migration(migrations.Migration):

    dependencies = [
        ('cephia', '0056_auto_20160810_1509'),
    ]

    operations = [
        migrations.RunPython(get_default_values, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='historicalvisit',
            name='scopevisit_ec',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='visit',
            name='scopevisit_ec',
            field=models.NullBooleanField(),
        ),
        migrations.RunPython(set_default_values, migrations.RunPython.noop),
    ]
