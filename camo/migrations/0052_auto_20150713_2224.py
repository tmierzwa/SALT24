# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0051_auto_20150712_1312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operation',
            name='aircraft',
        ),
        migrations.DeleteModel(
            name='Operation',
        ),
        migrations.AlterField(
            model_name='work_order',
            name='date',
            field=models.DateField(default=datetime.date(2015, 7, 13)),
            preserve_default=True,
        ),
    ]
