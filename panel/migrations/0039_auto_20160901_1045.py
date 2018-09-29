# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0038_auto_20160830_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duty',
            name='time_factor',
            field=models.DecimalField(verbose_name='Mnożnik czasu', max_digits=3, default=1, decimal_places=2),
        ),
    ]
