# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0022_auto_20160308_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdt',
            name='pre_cycles',
            field=models.IntegerField(blank=True, verbose_name='Suma cykli z przeniesienia', null=True, default=0),
        ),
        migrations.AddField(
            model_name='pdt',
            name='prev_landings',
            field=models.IntegerField(blank=True, verbose_name='Suma lądowań z przenisienia', null=True, default=0),
        ),
        migrations.AddField(
            model_name='pdt',
            name='prev_tth',
            field=models.DecimalField(verbose_name='Suma TTH z przeniesienia', max_digits=7, decimal_places=2, blank=True, null=True, default=0),
        ),
    ]
