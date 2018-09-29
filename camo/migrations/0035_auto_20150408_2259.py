# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0034_auto_20150407_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crs',
            name='done_date',
            field=models.DateField(default=datetime.date(2015, 4, 8)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pot_event',
            name='name',
            field=models.CharField(max_length=600),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='work_order',
            name='date',
            field=models.DateField(default=datetime.date(2015, 4, 8)),
            preserve_default=True,
        ),
    ]
