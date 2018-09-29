# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0013_pdt_available_fuel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operation',
            old_name='oil_lh_refill',
            new_name='oil_refill',
        ),
        migrations.RemoveField(
            model_name='operation',
            name='hydr_oil_state',
        ),
        migrations.RemoveField(
            model_name='operation',
            name='oil_rh_refill',
        ),
        migrations.RemoveField(
            model_name='operation',
            name='oil_state',
        ),
        migrations.RemoveField(
            model_name='operation',
            name='trans_oil_state',
        ),
        migrations.AddField(
            model_name='operation',
            name='Liczba cykli',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='operation',
            name='fuel_source',
            field=models.CharField(max_length=10, verbose_name='Źródło paliwa', default='unknown'),
        ),
        migrations.AlterField(
            model_name='operation',
            name='landings',
            field=models.IntegerField(verbose_name='Liczba lądowań', default=1),
        ),
        migrations.AlterField(
            model_name='pdt',
            name='open_user',
            field=models.ForeignKey(to='panel.FBOUser', verbose_name='Otwarty przez', related_name='pdt_open_by_set'),
        ),
    ]
