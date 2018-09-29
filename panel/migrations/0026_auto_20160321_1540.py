# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0025_pdt_ms_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='duty',
            name='block_time_factor',
            field=models.DecimalField(default=1, verbose_name='Mnożnik czasu służby', max_digits=3, decimal_places=2),
        ),
        migrations.AddField(
            model_name='duty',
            name='block_time_from',
            field=models.TimeField(verbose_name='Godzina rozpoczęcia służby', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='duty',
            name='block_time_to',
            field=models.TimeField(verbose_name='Godzina zakończenia służby', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='duty',
            name='duty_time_from',
            field=models.TimeField(verbose_name='Godzina rozpoczęcia pracy', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='duty',
            name='duty_time_to',
            field=models.TimeField(verbose_name='Godzina zakończenia pracy', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='duty',
            name='block_time',
            field=models.DurationField(default=0, verbose_name='Czas służby', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='duty',
            name='duty_time',
            field=models.DurationField(verbose_name='Czas pracy'),
        ),
        migrations.AlterField(
            model_name='duty',
            name='remarks',
            field=models.TextField(verbose_name='Uwagi', blank=True, null=True),
        ),
    ]
