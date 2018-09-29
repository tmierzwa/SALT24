# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0043_auto_20150411_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='crs',
            field=models.CharField(null=True, blank=True, max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='work_order',
            name='date',
            field=models.DateField(default=datetime.date(2015, 4, 12)),
            preserve_default=True,
        ),
    ]
