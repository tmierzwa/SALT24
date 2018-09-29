# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0015_auto_20150728_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duty',
            name='block_time',
            field=models.DecimalField(verbose_name='Czas służby', null=True, default=0, max_digits=4, blank=True, decimal_places=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='operation',
            name='operation_type',
            field=models.CharField(verbose_name='Rodzaj lotu', max_length=3, choices=[('01', '01 - Przewóz lotniczy (AOC)'), ('02', '02 - Usługi lotnicze (AWC)'), ('03A', '03A - Szkolenie w ramach AOC'), ('03B', '03B - Szkolenie w ramach ATO'), ('04', '04 - Wynajem SP'), ('05', '05 - Loty niepłatne (AOC)')]),
            preserve_default=True,
        ),
    ]
