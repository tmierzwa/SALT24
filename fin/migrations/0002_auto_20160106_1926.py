# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fueltank',
            name='tank_ref',
            field=models.CharField(default='brak', verbose_name='Symbol zbiornika', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fueltank',
            name='name',
            field=models.CharField(verbose_name='Nazwa zbiornika', max_length=50),
        ),
        migrations.AlterField(
            model_name='fueltransfer',
            name='fueltank_from',
            field=models.ForeignKey(to='fin.FuelTank', verbose_name='Zbiornik żródłowy', related_name='out_transfers'),
        ),
        migrations.AlterField(
            model_name='fueltransfer',
            name='fueltank_to',
            field=models.ForeignKey(to='fin.FuelTank', verbose_name='Zbiornik docelowy', related_name='in_transfers'),
        ),
    ]
