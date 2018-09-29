# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ato', '0002_auto_20150904_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='restrictions',
            field=models.CharField(choices=[('TAK', 'TAK'), ('NIE', 'NIE')], verbose_name='Restrykcje na instruktora', max_length=3, default='NIE'),
        ),
    ]
