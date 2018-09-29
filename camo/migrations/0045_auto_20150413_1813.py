# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0044_auto_20150412_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='part_no',
            field=models.CharField(verbose_name='Numer części (Typ)', max_length=30, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='work_order',
            name='date',
            field=models.DateField(default=datetime.date(2015, 4, 13)),
            preserve_default=True,
        ),
    ]
