# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-01-22 20:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geneseekr', '0009_geneseekrrequest_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geneseekrrequest',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
