# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0082_pot_group_applies'),
    ]

    operations = [
        migrations.AddField(
            model_name='aircraft',
            name='fuel_consumption',
            field=models.DecimalField(verbose_name='Zużycie paliwa (L/h)', max_digits=4, default=0, decimal_places=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aircraft',
            name='fuel_type',
            field=models.CharField(max_length=5, verbose_name='Rodzaj paliwa', choices=[('AVGAS', 'Avgas 100LL'), ('MOGAS', 'Benzyna samochodowa'), ('JETA1', 'Paliwo JET A-1')], default='AVGAS'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aircraft',
            name='fuel_volume',
            field=models.DecimalField(verbose_name='Szacowana ilość paliwa (L)', max_digits=4, default=0, decimal_places=1),
        ),
    ]
