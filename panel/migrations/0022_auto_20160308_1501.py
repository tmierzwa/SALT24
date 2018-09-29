# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0021_auto_20160308_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operation',
            name='fuel_after',
        ),
        migrations.RemoveField(
            model_name='operation',
            name='fuel_after_source',
        ),
        migrations.AddField(
            model_name='pdt',
            name='fuel_after',
            field=models.IntegerField(blank=True, verbose_name='Paliwo zatankowane po locie', null=True),
        ),
        migrations.AddField(
            model_name='pdt',
            name='fuel_after_source',
            field=models.CharField(verbose_name='Źródło paliwa po locie', max_length=10, default='unknown'),
        ),
    ]
