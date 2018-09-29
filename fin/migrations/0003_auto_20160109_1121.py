# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fin', '0002_auto_20160106_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fueltransfer',
            name='liter_price',
            field=models.FloatField(verbose_name='Średnia cena za litr (PLN)'),
        ),
    ]
