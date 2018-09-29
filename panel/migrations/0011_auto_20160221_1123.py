# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0010_auto_20160219_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdt',
            name='tth_end',
            field=models.DecimalField(max_digits=7, null=True, blank=True, verbose_name='Licznik końcowy', decimal_places=2),
        ),
        migrations.AddField(
            model_name='pdt',
            name='tth_start',
            field=models.DecimalField(max_digits=7, default=0, decimal_places=2, verbose_name='Licznik początkowy'),
            preserve_default=False,
        ),
    ]
