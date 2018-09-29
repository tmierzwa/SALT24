# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fin', '0015_auto_20160318_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remotefueling',
            name='total_price',
            field=models.DecimalField(decimal_places=2, null=True, blank=True, max_digits=7, verbose_name='Wartość paliwa (PLN)'),
        ),
    ]
