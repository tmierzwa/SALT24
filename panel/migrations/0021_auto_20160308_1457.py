# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0020_auto_20160308_0836'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='fuel_after',
            field=models.IntegerField(null=True, blank=True, verbose_name='Paliwo zatankowane po locie'),
        ),
        migrations.AddField(
            model_name='operation',
            name='fuel_after_source',
            field=models.CharField(max_length=10, verbose_name='Źródło paliwa po locie', default='unknown'),
        ),
        migrations.AlterField(
            model_name='operation',
            name='landings',
            field=models.IntegerField(default=0, blank=True, verbose_name='Liczba lądowań', null=True),
        ),
    ]
