# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0019_auto_20160308_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='fuel_used',
            field=models.IntegerField(verbose_name='Paliwo zużyte', null=True, blank=True),
        ),
    ]
