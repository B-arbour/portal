# Generated by Django 2.2.13 on 2020-08-25 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primer_finder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='primerfinder',
            name='primer_seq',
            field=models.CharField(blank=True, choices=[('custom', 'Custom EPCR'), ('vtyper', 'Verotoxin')], default='custom', max_length=200),
        ),
    ]
