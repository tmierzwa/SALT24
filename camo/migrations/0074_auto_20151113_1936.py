# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0073_auto_20151028_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='part_no',
            field=models.CharField(verbose_name='Numer części (typ)', max_length=35),
        ),
        migrations.AlterField(
            model_name='part',
            name='serial_no',
            field=models.CharField(verbose_name='Numer seryjny', max_length=35),
        ),
    ]
