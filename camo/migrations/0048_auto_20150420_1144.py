# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0047_auto_20150419_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraft',
            name='insurance_date',
            field=models.DateField(verbose_name='Ważność ubezp.', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='radio_date',
            field=models.DateField(verbose_name='Ważność radia', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='assignment',
            name='crs',
            field=models.CharField(null=True, max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='assignment',
            name='description',
            field=models.CharField(null=True, max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='work_order',
            name='date',
            field=models.DateField(default=datetime.date(2015, 4, 20)),
            preserve_default=True,
        ),
    ]
