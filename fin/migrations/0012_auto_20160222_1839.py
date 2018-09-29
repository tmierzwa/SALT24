# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0011_auto_20160221_1123'),
        ('fin', '0011_auto_20160114_1141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fuelburn',
            name='pdt_operation',
        ),
        migrations.AddField(
            model_name='fuelburn',
            name='pdt',
            field=models.ForeignKey(default=1, verbose_name='Powiązany PDT', to='panel.PDT'),
            preserve_default=False,
        ),
    ]
