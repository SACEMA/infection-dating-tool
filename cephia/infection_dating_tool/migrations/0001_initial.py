# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-04-20 08:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import lib.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='IDTAllowedRegistrationEmails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=200, null=True, unique=True)),
            ],
            options={
                'db_table': 'idt_allowed_registration_emails',
            },
        ),
        migrations.CreateModel(
            name='IDTDiagnosticTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(blank=True, choices=[('1st_gen_lab', '1st Gen Lab Assay (Viral Lysate IgG sensitive Antibody)'), ('2nd_gen_lab', '2nd Gen Lab Assay (Recombinant IgG sensitive Antibody)'), ('2nd_gen_rapid', '2nd Gen Rapid Test'), ('3rd_gen_lab', '3rd Gen Lab Assay (IgM sensitive Antibody)'), ('3rd_gen_rapid', '3rd Gen Rapid Test'), ('4th_gen_lab', '4th Gen Lab Assay (p24 Ag/Ab Combo)'), ('4th_gen_rapid', '4th Gen Rapid Test'), ('dpp', 'DPP'), ('immunofluorescence_assay', 'Immunofluorescence Assay'), ('p24_antigen', 'p24 Antigen'), ('viral_load', 'Viral Load'), ('western_blot', 'Western blot')], max_length=255, null=True)),
                ('user', lib.fields.ProtectedForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'idt_diagnostic_tests',
            },
        ),
        migrations.CreateModel(
            name='IDTDiagnosticTestHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_code', models.CharField(blank=True, max_length=255, null=True)),
                ('test_date', models.DateField(null=True)),
                ('adjusted_date', models.DateField(null=True)),
                ('test_result', models.CharField(max_length=15, null=True)),
            ],
            options={
                'db_table': 'idt_diagnostic_test_history',
            },
        ),
        migrations.CreateModel(
            name='IDTFileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_file', models.FileField(upload_to='/home/andrew/id/idt_prod/cephia/cephia/../../media/infection_dating_tool_uploads')),
                ('file_name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('state', models.CharField(choices=[('pending', 'Pending'), ('imported', 'Imported'), ('validated', 'Validated'), ('needs_mapping', 'Needs Mapping'), ('mapped', 'Mapped'), ('error', 'Error')], default='pending', max_length=15)),
                ('message', models.TextField(blank=True)),
                ('deleted', models.BooleanField(default=False)),
                ('user', lib.fields.ProtectedForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'idt_file_info',
            },
        ),
        migrations.CreateModel(
            name='IDTSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_label', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('edsc_reported', models.DateField(blank=True, default=None, null=True)),
                ('ep_ddi', models.DateField(blank=True, null=True)),
                ('lp_ddi', models.DateField(blank=True, null=True)),
                ('interval_size', models.IntegerField(blank=True, null=True)),
                ('edsc_days_difference', models.IntegerField(blank=True, null=True)),
                ('eddi', models.DateField(blank=True, null=True)),
                ('flag', models.CharField(max_length=255, null=True)),
                ('user', lib.fields.ProtectedForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='subjects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'idt_subjects',
            },
        ),
        migrations.CreateModel(
            name='IDTTestPropertyEstimate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_default', models.BooleanField(default=False)),
                ('global_default', models.BooleanField(default=False)),
                ('estimate_label', models.CharField(blank=True, max_length=255)),
                ('comment', models.CharField(blank=True, max_length=255)),
                ('diagnostic_delay', models.FloatField(null=True)),
                ('diagnostic_delay_mean', models.FloatField(null=True)),
                ('diagnostic_delay_mean_se', models.FloatField(null=True)),
                ('diagnostic_delay_mean_ci_lower', models.FloatField(null=True)),
                ('diagnostic_delay_mean_ci_upper', models.FloatField(null=True)),
                ('diagnostic_delay_median', models.FloatField(null=True)),
                ('diagnostic_delay_median_se', models.FloatField(null=True)),
                ('diagnostic_delay_median_ci_lower', models.FloatField(null=True)),
                ('diagnostic_delay_median_ci_upper', models.FloatField(null=True)),
                ('diagnostic_delay_range', models.CharField(blank=True, max_length=255, null=True)),
                ('diagnostic_delay_iqr', models.CharField(blank=True, max_length=255, null=True)),
                ('test', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='infection_dating_tool.IDTDiagnosticTest')),
                ('user', lib.fields.ProtectedForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'idt_test_property_estimates',
            },
        ),
        migrations.CreateModel(
            name='TestPropertyMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('test', lib.fields.ProtectedForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='infection_dating_tool.IDTDiagnosticTest')),
                ('test_property', lib.fields.ProtectedForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='infection_dating_tool.IDTTestPropertyEstimate')),
                ('user', lib.fields.ProtectedForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'idt_test_property_mapping',
            },
        ),
        migrations.AddField(
            model_name='idtdiagnostictesthistory',
            name='data_file',
            field=lib.fields.ProtectedForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='test_history', to='infection_dating_tool.IDTFileInfo'),
        ),
        migrations.AddField(
            model_name='idtdiagnostictesthistory',
            name='subject',
            field=lib.fields.ProtectedForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='idt_test_history', to='infection_dating_tool.IDTSubject'),
        ),
        migrations.AlterUniqueTogether(
            name='testpropertymapping',
            unique_together=set([('code', 'user')]),
        ),
        migrations.AlterUniqueTogether(
            name='idtsubject',
            unique_together=set([('subject_label', 'user')]),
        ),
        migrations.AlterUniqueTogether(
            name='idtdiagnostictest',
            unique_together=set([('name', 'user')]),
        ),
    ]
