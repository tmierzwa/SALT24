# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0029_auto_20150405_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modification',
            name='remarks',
            field=models.CharField(max_length=500, null=True, verbose_name='Uwagi', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='wb_report',
            name='remarks',
            field=models.CharField(max_length=500, null=True, verbose_name='Uwagi', blank=True),
            preserve_default=True,
        ),
    ]
