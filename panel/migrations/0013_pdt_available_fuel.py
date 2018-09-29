# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0012_auto_20160222_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdt',
            name='available_fuel',
            field=models.DecimalField(decimal_places=1, verbose_name='Ilość paliwa do lotu', max_digits=4, default=0),
        ),
    ]
