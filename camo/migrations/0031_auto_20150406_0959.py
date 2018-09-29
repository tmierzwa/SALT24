# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0030_auto_20150405_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='aircraft',
            name='mtow',
            field=models.IntegerField(default=750, verbose_name='MTOW'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='crs',
            name='done_date',
            field=models.DateField(default=datetime.date(2015, 4, 6)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='work_order',
            name='date',
            field=models.DateField(default=datetime.date(2015, 4, 6)),
            preserve_default=True,
        ),
    ]
