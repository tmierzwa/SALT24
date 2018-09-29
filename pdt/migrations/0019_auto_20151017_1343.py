# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0018_auto_20150813_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='tth_end',
            field=models.DecimalField(decimal_places=2, verbose_name='Licznik końcowy', max_digits=7),
        ),
        migrations.AlterField(
            model_name='operation',
            name='tth_start',
            field=models.DecimalField(decimal_places=2, verbose_name='Licznik początkowy', max_digits=7),
        ),
    ]
