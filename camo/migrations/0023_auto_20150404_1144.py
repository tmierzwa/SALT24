# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0022_auto_20150403_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='aircraft',
            name='status',
            field=models.CharField(choices=[('flying', 'W użytkowaniu'), ('parked', 'Hangarowany')], max_length=10, default='flying'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='crs',
            name='done_date',
            field=models.DateField(default=datetime.date(2015, 4, 4)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='work_order',
            name='date',
            field=models.DateField(default=datetime.date(2015, 4, 4)),
            preserve_default=True,
        ),
    ]
