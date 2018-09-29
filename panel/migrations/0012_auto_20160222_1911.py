# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0011_auto_20160221_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdt',
            name='cycles',
            field=models.IntegerField(verbose_name='Suma cykli', default=1),
        ),
        migrations.AddField(
            model_name='pdt',
            name='landings',
            field=models.IntegerField(verbose_name='Suma lądowań', default=1),
        ),
    ]
