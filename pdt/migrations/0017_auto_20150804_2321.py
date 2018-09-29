# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0016_auto_20150729_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='operation_type',
            field=models.CharField(max_length=3, choices=[('01', '01 - Przewóz lotniczy'), ('02', '02 - Usługi lotnicze'), ('03A', '03A - Szkolenie AOC'), ('03B', '03B - Szkolenie ATO'), ('04', '04 - Wynajem SP'), ('05', '05 - Loty niepłatne')], verbose_name='Rodzaj lotu'),
            preserve_default=True,
        ),
    ]
