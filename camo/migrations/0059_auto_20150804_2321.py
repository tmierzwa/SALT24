# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0058_auto_20150729_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work_order',
            name='date',
            field=models.DateField(default=datetime.date(2015, 8, 4)),
            preserve_default=True,
        ),
    ]
