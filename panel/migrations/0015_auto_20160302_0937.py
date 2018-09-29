# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0014_auto_20160225_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='fuel_source',
            field=models.CharField(verbose_name='Źródło paliwa', max_length=10, default='unknown', choices=[('SALT', 'SALT')]),
        ),
    ]
