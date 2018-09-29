# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ato', '0012_auto_20150908_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='code',
            field=models.CharField(verbose_name='Kod ćwiczenia', max_length=12),
        ),
        migrations.AlterField(
            model_name='phase',
            name='code',
            field=models.CharField(verbose_name='Kod zadania/fazy', max_length=12),
        ),
    ]
