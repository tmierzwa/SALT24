# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0071_auto_20151017_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='MS_report',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('ms_ref', models.CharField(max_length=20, verbose_name='Numer MS')),
                ('fuselage', models.CharField(max_length=30, verbose_name='Numer płatowca')),
                ('engine1', models.CharField(max_length=30, verbose_name='Numer silnika L')),
                ('engine2', models.CharField(blank=True, null=True, max_length=30, verbose_name='Numer silnika R')),
                ('ms_date', models.DateField(verbose_name='Data MS')),
                ('hours', models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Liczba godzin')),
                ('landings', models.IntegerField(verbose_name='Liczbą lądowań')),
                ('crs_ref', models.CharField(blank=True, null=True, max_length=20, verbose_name='Numer CRS')),
                ('crs_date', models.DateField(blank=True, null=True, verbose_name='Data CRS')),
                ('next_hours', models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Ważne do nalotu')),
                ('next_date', models.DateField(verbose_name='Ważne do daty')),
                ('remarks', models.TextField(blank=True, null=True, verbose_name='Uwagi')),
                ('aircraft', models.ForeignKey(to='camo.Aircraft', verbose_name='Statek powietrzny')),
            ],
        ),
    ]
