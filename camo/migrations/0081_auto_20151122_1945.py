# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0080_auto_20151120_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraft',
            name='use_cycles',
            field=models.BooleanField(default=False, verbose_name='Używaj cykli'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='use_landings',
            field=models.BooleanField(default=False, verbose_name='Używaj lądowań'),
        ),
        migrations.AlterField(
            model_name='ms_report',
            name='done_cycles',
            field=models.IntegerField(default=0, verbose_name='Liczba cykli'),
        ),
        migrations.AlterField(
            model_name='ms_report',
            name='done_landings',
            field=models.IntegerField(default=0, verbose_name='Liczba lądowań'),
        ),
        migrations.AlterField(
            model_name='ms_report',
            name='next_cycles',
            field=models.IntegerField(verbose_name='Ważne do liczby cykli', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ms_report',
            name='next_landings',
            field=models.IntegerField(verbose_name='Ważne do liczby lądowań', blank=True, null=True),
        ),
    ]
