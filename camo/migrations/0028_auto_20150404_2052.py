# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0027_auto_20150404_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='pot_group',
            name='adsb_agency',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Organ wydający'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pot_group',
            name='adsb_date',
            field=models.DateField(blank=True, verbose_name='Data AD/SB', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pot_group',
            name='adsb_no',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Numer AD/SB'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pot_group',
            name='remarks',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Uwagi'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pot_group',
            name='type',
            field=models.CharField(default='oth', max_length=10, choices=[('oth', 'Obsługa techniczna'), ('llp', 'Planowy demontaż'), ('ovh', 'Planowy remont'), ('ad', 'AD - Dyrektywa'), ('sb', 'SB - Biuletyn')], verbose_name='Rodzaj czynności'),
            preserve_default=True,
        ),
    ]
