# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0010_auto_20150725_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='fuel_used',
            field=models.IntegerField(default=0, verbose_name='Paliwo zu?yte'),
            preserve_default=False,
        ),
    ]
