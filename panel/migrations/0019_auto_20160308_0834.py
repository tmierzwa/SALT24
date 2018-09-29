# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0018_auto_20160307_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='status',
            field=models.CharField(max_length=10, choices=[('open', 'Otwarta'), ('closed', 'Zamknięta')], verbose_name='Status', default='open'),
        ),
        migrations.AlterField(
            model_name='operation',
            name='cycles',
            field=models.IntegerField(null=True, verbose_name='Liczba cykli', blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='operation',
            name='landings',
            field=models.IntegerField(null=True, verbose_name='Liczba lądowań', blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='operation',
            name='loc_end',
            field=models.CharField(null=True, max_length=20, verbose_name='Miejsce lądowania', blank=True),
        ),
        migrations.AlterField(
            model_name='operation',
            name='loc_start',
            field=models.CharField(null=True, max_length=20, verbose_name='Miejsce startu', blank=True),
        ),
        migrations.AlterField(
            model_name='operation',
            name='time_end',
            field=models.TimeField(null=True, verbose_name='Czas on-block', blank=True),
        ),
        migrations.AlterField(
            model_name='operation',
            name='time_start',
            field=models.TimeField(null=True, verbose_name='Czas off-block', blank=True),
        ),
        migrations.AlterField(
            model_name='operation',
            name='tth_end',
            field=models.DecimalField(null=True, decimal_places=2, max_digits=7, verbose_name='Licznik końcowy', blank=True),
        ),
    ]
