# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0046_auto_20150416_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='aircraft',
            name='arc_date',
            field=models.DateField(verbose_name='Ważność ARC', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aircraft',
            name='radio_date',
            field=models.DateField(verbose_name='Ważność pozwolenia radiowego', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='insurance_date',
            field=models.DateField(verbose_name='Ważność ubezpieczenia', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='work_order',
            name='date',
            field=models.DateField(default=datetime.date(2015, 4, 19)),
            preserve_default=True,
        ),
    ]
