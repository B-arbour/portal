# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-09-04 15:25
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import olc_webportalv2.cowbat.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AzureTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exit_code_file', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='DataFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_file', models.FileField(upload_to=olc_webportalv2.cowbat.models.get_run_name)),
            ],
        ),
        migrations.CreateModel(
            name='InterOpFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interop_file', models.FileField(upload_to=olc_webportalv2.cowbat.models.get_interop_name)),
            ],
        ),
        migrations.CreateModel(
            name='SequencingRun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run_name', models.CharField(max_length=64)),
                ('status', models.CharField(default='Unprocessed', max_length=64)),
                ('seqids', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=24), blank=True, default=[], size=None)),
                ('download_link', models.CharField(blank=True, default='', max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='interopfile',
            name='sequencing_run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interop', to='cowbat.SequencingRun'),
        ),
        migrations.AddField(
            model_name='datafile',
            name='sequencing_run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datafile', to='cowbat.SequencingRun'),
        ),
        migrations.AddField(
            model_name='azuretask',
            name='sequencing_run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='azuretask', to='cowbat.SequencingRun'),
        ),
    ]
