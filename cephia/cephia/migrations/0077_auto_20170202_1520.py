# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-02 13:20
from __future__ import unicode_literals

from django.db import migrations, models
import random

def blinded_label_generator():
    random_number = str(random.randint(10000000, 99999999))
    return random_number

def apply_blinded_labels(apps, schema):
    Subject = apps.get_model('cephia', 'Subject')
    subjects = Subject.objects.all()
    for subject in subjects:
        if not subject.subject_label_blinded:
            subject.subject_label_blinded = blinded_label_generator()
            while Subject.objects.filter(subject_label_blinded=subject.subject_label_blinded).exists():
                subject.subject_label_blinded = blinded_label_generator()
        subject.save()

class Migration(migrations.Migration):

    dependencies = [
        ('cephia', '0076_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalsubject',
            name='subject_label_blinded',
            field=models.CharField(blank=True, db_index=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='subject_label_blinded',
            field=models.CharField(blank=True, db_index=True, max_length=25, null=True, unique=True),
        ),
        migrations.RunPython(apply_blinded_labels, migrations.RunPython.noop)
    ]
