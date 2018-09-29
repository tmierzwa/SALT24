# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0040_operation_remarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pot_group',
            name='done_aso',
            field=models.ForeignKey(to='camo.ASO', blank=True, null=True, verbose_name='Organizacja'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='wb_report',
            name='done_doc',
            field=models.CharField(blank=True, max_length=20, verbose_name='Numer CRS', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='work_order',
            name='date',
            field=models.DateField(default=datetime.date(2015, 4, 10)),
            preserve_default=True,
        ),
    ]
