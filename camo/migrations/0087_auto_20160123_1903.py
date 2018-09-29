# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0086_aircraft_rent_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraft',
            name='rent_price',
            field=models.DecimalField(verbose_name='Cena wynajmu (PLN/h)', max_digits=7, default=0, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='part',
            name='production_date',
            field=models.DateField(verbose_name='Data produkcji', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='wb_report',
            name='lat_cg',
            field=models.DecimalField(max_digits=9, verbose_name='Lateral C.G.', null=True, blank=True, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='wb_report',
            name='lat_moment',
            field=models.DecimalField(max_digits=9, verbose_name='Lateral moment', null=True, blank=True, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='wb_report',
            name='lon_cg',
            field=models.DecimalField(max_digits=9, verbose_name='Longitudal C.G.', null=True, blank=True, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='wb_report',
            name='lon_moment',
            field=models.DecimalField(max_digits=9, verbose_name='Longitudal moment', null=True, blank=True, decimal_places=3),
        ),
    ]
