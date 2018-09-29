# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0090_auto_20160127_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='aircraft',
            name='fuel_capacity',
            field=models.DecimalField(max_digits=4, verbose_name='Zbiornik paliwa (L)', default=0, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='fuel_consumption',
            field=models.DecimalField(max_digits=4, verbose_name='Zużycie paliwa (L/h)', default=0, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='status',
            field=models.CharField(choices=[('flying', 'W użytkowaniu'), ('damaged', 'Uszkodzony'), ('parked', 'Zaparkowany')], max_length=10),
        ),
    ]
