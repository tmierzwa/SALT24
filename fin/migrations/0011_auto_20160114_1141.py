# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fin', '0010_soldpackage_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuelburn',
            name='pdt_operation',
            field=models.ForeignKey(verbose_name='Operacja PDT', to='panel.Operation'),
        ),
        migrations.AlterField(
            model_name='pdtfueling',
            name='pdt',
            field=models.ForeignKey(verbose_name='PDT', to='panel.PDT'),
        ),
        migrations.AlterField(
            model_name='remotefueling',
            name='pdt',
            field=models.ForeignKey(verbose_name='PDT', to='panel.PDT'),
        ),
    ]
