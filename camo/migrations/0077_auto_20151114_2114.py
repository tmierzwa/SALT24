# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0076_auto_20151114_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wb_report',
            name='aso',
            field=models.CharField(max_length=100, verbose_name='Organizacja'),
        ),
    ]
