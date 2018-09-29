# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0007_auto_20150713_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdt',
            name='open_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Czas otwarcia'),
            preserve_default=True,
        ),
    ]
