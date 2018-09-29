# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import salt.models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0035_auto_20160815_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duty',
            name='block_time',
            field=salt.models.MyDurationField(null=True, verbose_name='Czas lotu', blank=True),
        ),
        migrations.AlterField(
            model_name='duty',
            name='block_time_factor',
            field=models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Mnożnik czasu lotu', default=1),
        ),
        migrations.AlterField(
            model_name='duty',
            name='block_time_from',
            field=models.TimeField(null=True, verbose_name='Rozpoczęcie lotu', blank=True),
        ),
        migrations.AlterField(
            model_name='duty',
            name='block_time_to',
            field=models.TimeField(null=True, verbose_name='Zakończenie lotu', blank=True),
        ),
        migrations.AlterField(
            model_name='duty',
            name='duty_time',
            field=salt.models.MyDurationField(verbose_name='Czas służby'),
        ),
        migrations.AlterField(
            model_name='duty',
            name='duty_time_from',
            field=models.TimeField(null=True, verbose_name='Rozpoczęcie służby', blank=True),
        ),
        migrations.AlterField(
            model_name='duty',
            name='duty_time_to',
            field=models.TimeField(null=True, verbose_name='Zakończenie służby', blank=True),
        ),
    ]
