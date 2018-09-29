# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0079_auto_20151114_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='aircraft',
            name='cycles_count',
            field=models.IntegerField(default=0, verbose_name='Licznik cykli'),
        ),
        migrations.AddField(
            model_name='aircraft',
            name='use_cycles',
            field=models.BooleanField(default=False, verbose_name='Użycie cykli'),
        ),
        migrations.AddField(
            model_name='aircraft',
            name='use_landings',
            field=models.BooleanField(default=False, verbose_name='Użycie lądowań'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='from_cycles',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='assignment',
            name='to_cycles',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='camo_operation',
            name='cycles',
            field=models.IntegerField(default=0, verbose_name='Liczba cykli'),
        ),
        migrations.AddField(
            model_name='modification',
            name='done_cycles',
            field=models.IntegerField(blank=True, verbose_name='Cykle wykonania', null=True),
        ),
        migrations.AddField(
            model_name='modification',
            name='done_landings',
            field=models.IntegerField(blank=True, verbose_name='Lądowania wykonania', null=True),
        ),
        migrations.AddField(
            model_name='ms_report',
            name='done_cycles',
            field=models.IntegerField(default=0, verbose_name='Liczbą lądowań'),
        ),
        migrations.AddField(
            model_name='ms_report',
            name='next_cycles',
            field=models.DateField(blank=True, verbose_name='Ważne do liczby cykli', null=True),
        ),
        migrations.AddField(
            model_name='ms_report',
            name='next_landings',
            field=models.DateField(blank=True, verbose_name='Ważne do liczby cykli', null=True),
        ),
        migrations.AddField(
            model_name='part',
            name='cycles_count',
            field=models.IntegerField(default=0, verbose_name='Licznik cykli'),
        ),
        migrations.AddField(
            model_name='pot_event',
            name='done_cycles',
            field=models.IntegerField(blank=True, verbose_name='Wykonano (cykle)', null=True),
        ),
        migrations.AddField(
            model_name='pot_group',
            name='done_cycles',
            field=models.IntegerField(blank=True, verbose_name='Wykonano (cykle)', null=True),
        ),
        migrations.AddField(
            model_name='pot_group',
            name='due_cycles',
            field=models.IntegerField(blank=True, verbose_name='Limit cykli', null=True),
        ),
        migrations.AddField(
            model_name='wb_report',
            name='done_cycles',
            field=models.IntegerField(blank=True, verbose_name='Cykle wykonania', null=True),
        ),
        migrations.AddField(
            model_name='wb_report',
            name='done_landings',
            field=models.IntegerField(blank=True, verbose_name='Lądowania wykonania', null=True),
        ),
        migrations.AddField(
            model_name='work_order_line',
            name='done_cycles',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='from_landings',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='camo_operation',
            name='landings',
            field=models.IntegerField(default=0, verbose_name='Liczba lądowań'),
        ),
        migrations.AlterField(
            model_name='ms_report',
            name='done_landings',
            field=models.IntegerField(default=0, verbose_name='Liczbą lądowań'),
        ),
    ]
