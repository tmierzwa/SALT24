# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fin', '0012_auto_20160222_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fuelburn',
            name='pdt',
        ),
        migrations.DeleteModel(
            name='FuelBurn',
        ),
    ]
