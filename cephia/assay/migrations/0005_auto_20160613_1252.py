# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-13 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assay', '0004_auto_20160609_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idev3result',
            name='conclusion_recalc',
        ),
        migrations.RemoveField(
            model_name='idev3result',
            name='intermediate',
        ),
        migrations.RemoveField(
            model_name='idev3result',
            name='ratioTM',
        ),
        migrations.RemoveField(
            model_name='idev3result',
            name='ratioV3',
        ),
        migrations.RemoveField(
            model_name='idev3resultrow',
            name='conclusion_recalc',
        ),
        migrations.RemoveField(
            model_name='idev3resultrow',
            name='idev3_result',
        ),
        migrations.RemoveField(
            model_name='idev3resultrow',
            name='intermediate',
        ),
        migrations.RemoveField(
            model_name='idev3resultrow',
            name='ratioTM',
        ),
        migrations.RemoveField(
            model_name='idev3resultrow',
            name='ratioV3',
        ),
        migrations.AddField(
            model_name='idev3result',
            name='conclusion_reported',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='idev3result',
            name='intermediaire_reported',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='idev3result',
            name='intermediare',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='idev3result',
            name='tm_ratio',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='idev3result',
            name='tm_ratio_reported',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='idev3result',
            name='v3_ratio',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='idev3result',
            name='v3_ratio_reported',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='idev3result',
            name='well_tm',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='idev3result',
            name='well_v3',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='idev3resultrow',
            name='conclusion_reported',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='idev3resultrow',
            name='intermediaire_reported',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='idev3resultrow',
            name='intermediare',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='idev3resultrow',
            name='tm_ratio',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='idev3resultrow',
            name='tm_ratio_reported',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='idev3resultrow',
            name='v3_ratio',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='idev3resultrow',
            name='v3_ratio_reported',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='idev3resultrow',
            name='well_tm',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='idev3resultrow',
            name='well_v3',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='architectavidityresult',
            name='interpretation',
            field=models.CharField(choices=[(b'recent', b'Recent'), (b'non_recent', b'Non-Recent')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='architectunmodifiedresult',
            name='interpretation',
            field=models.CharField(choices=[(b'recent', b'Recent'), (b'non_recent', b'Non-Recent')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bedresult',
            name='interpretation',
            field=models.CharField(choices=[(b'recent', b'Recent'), (b'non_recent', b'Non-Recent')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bioradaviditycdcresult',
            name='interpretation',
            field=models.CharField(choices=[(b'recent', b'Recent'), (b'non_recent', b'Non-Recent')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bioradavidityglasgowresult',
            name='interpretation',
            field=models.CharField(choices=[(b'recent', b'Recent'), (b'non_recent', b'Non-Recent')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bioradavidityjhuresult',
            name='interpretation',
            field=models.CharField(choices=[(b'recent', b'Recent'), (b'non_recent', b'Non-Recent')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='geeniusresult',
            name='interpretation',
            field=models.CharField(choices=[(b'recent', b'Recent'), (b'non_recent', b'Non-Recent')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='idev3result',
            name='interpretation',
            field=models.CharField(choices=[(b'recent', b'Recent'), (b'non_recent', b'Non-Recent')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='idev3resultrow',
            name='conclusion',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='idev3resultrow',
            name='tm_OD',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='idev3resultrow',
            name='v3_OD',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='lagmaximresult',
            name='interpretation',
            field=models.CharField(choices=[(b'recent', b'Recent'), (b'non_recent', b'Non-Recent')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='lagsediaresult',
            name='interpretation',
            field=models.CharField(choices=[(b'recent', b'Recent'), (b'non_recent', b'Non-Recent')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='lsvitrosdiluentresult',
            name='interpretation',
            field=models.CharField(choices=[(b'recent', b'Recent'), (b'non_recent', b'Non-Recent')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='lsvitrosplasmaresult',
            name='interpretation',
            field=models.CharField(choices=[(b'recent', b'Recent'), (b'non_recent', b'Non-Recent')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='luminexcdcresult',
            name='interpretation',
            field=models.CharField(choices=[(b'recent', b'Recent'), (b'non_recent', b'Non-Recent')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='vitrosavidityresult',
            name='interpretation',
            field=models.CharField(choices=[(b'recent', b'Recent'), (b'non_recent', b'Non-Recent')], max_length=255, null=True),
        ),
    ]