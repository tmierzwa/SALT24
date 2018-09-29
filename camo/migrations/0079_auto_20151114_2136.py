# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0078_auto_20151114_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work_order',
            name='aso',
            field=models.CharField(max_length=100),
        ),
    ]
