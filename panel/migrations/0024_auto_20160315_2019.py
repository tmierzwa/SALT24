# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0023_auto_20160308_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='fuel_available',
            field=models.IntegerField(verbose_name='Stan paliwa do lotu (L)'),
        ),
        migrations.AlterField(
            model_name='operation',
            name='fuel_refill',
            field=models.IntegerField(verbose_name='Uzupełnione paliwo (L)', default=0),
        ),
        migrations.AlterField(
            model_name='operation',
            name='fuel_used',
            field=models.IntegerField(null=True, verbose_name='Paliwo zużyte (L)', blank=True),
        ),
        migrations.AlterField(
            model_name='operation',
            name='hydr_oil_refill',
            field=models.DecimalField(max_digits=3, verbose_name='Uzup. olej hydr. (qt)', default=0, blank=True, decimal_places=1, null=True),
        ),
        migrations.AlterField(
            model_name='operation',
            name='oil_refill',
            field=models.DecimalField(max_digits=3, verbose_name='Uzupełniony olej (qt)', default=0, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='operation',
            name='trans_oil_refill',
            field=models.DecimalField(max_digits=3, verbose_name='Uzup. olej przekł. (qt)', default=0, blank=True, decimal_places=1, null=True),
        ),
        migrations.AlterField(
            model_name='pdt',
            name='fuel_after',
            field=models.IntegerField(null=True, verbose_name='Paliwo uzup. po locie (L)', blank=True),
        ),
    ]
