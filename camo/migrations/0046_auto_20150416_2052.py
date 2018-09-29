# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0045_auto_20150413_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='super_ass',
            field=models.ForeignKey(blank=True, to='camo.Assignment', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='part',
            name='part_no',
            field=models.CharField(verbose_name='Numer części (typ)', max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='work_order',
            name='date',
            field=models.DateField(default=datetime.date(2015, 4, 16)),
            preserve_default=True,
        ),
    ]
