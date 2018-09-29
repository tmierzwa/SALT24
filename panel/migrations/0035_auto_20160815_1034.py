# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0034_remove_duty_my_duty_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdt',
            name='prev_landings',
            field=models.IntegerField(blank=True, verbose_name='Suma lądowań z przeniesienia', null=True, default=0),
        ),
    ]
