# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0094_auto_20160225_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='aircraft',
            name='last_pdt_ref',
            field=models.IntegerField(default=0, verbose_name='Ostatni numer PDT'),
        ),
        migrations.AddField(
            model_name='aircraft',
            name='ms_cycles',
            field=models.IntegerField(blank=True, verbose_name='MS do cykli', null=True),
        ),
        migrations.AddField(
            model_name='aircraft',
            name='ms_date',
            field=models.DateField(blank=True, verbose_name='MS do daty', null=True),
        ),
        migrations.AddField(
            model_name='aircraft',
            name='ms_hours',
            field=models.DecimalField(blank=True, decimal_places=2, verbose_name='MS do TTH', null=True, max_digits=7),
        ),
        migrations.AddField(
            model_name='aircraft',
            name='ms_landings',
            field=models.IntegerField(blank=True, verbose_name='MS do lądowań', null=True),
        ),
        migrations.AddField(
            model_name='aircraft',
            name='tth',
            field=models.DecimalField(decimal_places=2, default=0, verbose_name='Stan licznika na SP', max_digits=7),
        ),
    ]
