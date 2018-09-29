# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0069_auto_20151017_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pot_event',
            name='name',
            field=models.TextField(verbose_name='Nazwa czynności'),
        ),
        migrations.AlterField(
            model_name='wb_report',
            name='empty_weight',
            field=models.DecimalField(verbose_name='Masa pustego', decimal_places=2, max_digits=6),
        ),
    ]
