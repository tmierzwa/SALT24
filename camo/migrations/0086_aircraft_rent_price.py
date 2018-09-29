# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0085_auto_20160114_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='aircraft',
            name='rent_price',
            field=models.DecimalField(decimal_places=2, default=0, verbose_name='Cena godziny wynajmu', max_digits=7),
        ),
    ]
