# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0095_auto_20160307_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraft',
            name='cycles_count',
            field=models.IntegerField(verbose_name='Suma cykli', default=0),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='hours_count',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Suma TTH', default=0),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='landings_count',
            field=models.IntegerField(verbose_name='Suma lądowań', default=0),
        ),
        migrations.AlterField(
            model_name='part',
            name='cycles_count',
            field=models.IntegerField(verbose_name='Suma cykli', default=0),
        ),
        migrations.AlterField(
            model_name='part',
            name='hours_count',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Suma TTH', default=0),
        ),
        migrations.AlterField(
            model_name='part',
            name='landings_count',
            field=models.IntegerField(verbose_name='Suma lądowań', default=0),
        ),
    ]
