# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0041_auto_20150410_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='aircraft',
            name='hours_count',
            field=models.DecimalField(verbose_name='Licznik TTH', default=0, max_digits=6, decimal_places=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aircraft',
            name='landings_count',
            field=models.IntegerField(verbose_name='Licznik lądowań', default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assignment',
            name='description',
            field=models.CharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assignment',
            name='from_landings',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assignment',
            name='to_landings',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='work_order_line',
            name='done_landings',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='work_order',
            name='date',
            field=models.DateField(default=datetime.date(2015, 4, 11)),
            preserve_default=True,
        ),
    ]
