# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assay', '0004_auto_20160407_1342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='architectavidityresult',
            old_name='well',
            new_name='well_untreated',
        ),
        migrations.RenameField(
            model_name='architectavidityresultrow',
            old_name='well',
            new_name='well_untreated',
        ),
        migrations.RenameField(
            model_name='architectunmodifiedresult',
            old_name='well',
            new_name='well_untreated',
        ),
        migrations.RenameField(
            model_name='architectunmodifiedresultrow',
            old_name='well',
            new_name='well_untreated',
        ),
        migrations.RenameField(
            model_name='bedresult',
            old_name='well',
            new_name='well_untreated',
        ),
        migrations.RenameField(
            model_name='bedresultrow',
            old_name='well',
            new_name='well_untreated',
        ),
        migrations.RenameField(
            model_name='bioradaviditycdcresult',
            old_name='well',
            new_name='well_untreated',
        ),
        migrations.RenameField(
            model_name='bioradaviditycdcresultrow',
            old_name='well',
            new_name='well_treated',
        ),
        migrations.RenameField(
            model_name='bioradavidityglasgowresult',
            old_name='well',
            new_name='well_untreated',
        ),
        migrations.RenameField(
            model_name='bioradavidityglasgowresultrow',
            old_name='well',
            new_name='well_untreated',
        ),
        migrations.RenameField(
            model_name='bioradavidityjhuresult',
            old_name='well',
            new_name='well_untreated',
        ),
        migrations.RenameField(
            model_name='bioradavidityjhuresultrow',
            old_name='well',
            new_name='well_untreated',
        ),
        migrations.RenameField(
            model_name='geeniusresult',
            old_name='well',
            new_name='well_untreated',
        ),
        migrations.RenameField(
            model_name='geeniusresultrow',
            old_name='well',
            new_name='well_untreated',
        ),
        migrations.RenameField(
            model_name='idev3result',
            old_name='well',
            new_name='well_untreated',
        ),
        migrations.RenameField(
            model_name='idev3resultrow',
            old_name='well',
            new_name='well_untreated',
        ),
        migrations.RenameField(
            model_name='lagmaximresult',
            old_name='well',
            new_name='well_untreated',
        ),
        migrations.RenameField(
            model_name='lagmaximresultrow',
            old_name='well',
            new_name='well_untreated',
        ),
        migrations.RenameField(
            model_name='lagsediaresult',
            old_name='well',
            new_name='well_untreated',
        ),
        migrations.RenameField(
            model_name='lagsediaresultrow',
            old_name='well',
            new_name='well_untreated',
        ),
        migrations.RenameField(
            model_name='lsvitrosdiluentresult',
            old_name='well',
            new_name='well_untreated',
        ),
        migrations.RenameField(
            model_name='lsvitrosdiluentresultrow',
            old_name='well',
            new_name='well_untreated',
        ),
        migrations.RenameField(
            model_name='lsvitrosplasmaresult',
            old_name='well',
            new_name='well_untreated',
        ),
        migrations.RenameField(
            model_name='lsvitrosplasmaresultrow',
            old_name='well',
            new_name='well_untreated',
        ),
        migrations.RenameField(
            model_name='luminexcdcresult',
            old_name='well',
            new_name='well_untreated',
        ),
        migrations.RenameField(
            model_name='luminexcdcresultrow',
            old_name='well',
            new_name='well_untreated',
        ),
        migrations.RenameField(
            model_name='vitrosavidityresult',
            old_name='well',
            new_name='well_untreated',
        ),
        migrations.RenameField(
            model_name='vitrosavidityresultrow',
            old_name='well',
            new_name='well_untreated',
        ),
        migrations.AddField(
            model_name='bioradaviditycdcresult',
            name='well_treated',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='bioradaviditycdcresultrow',
            name='well_untreated',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]