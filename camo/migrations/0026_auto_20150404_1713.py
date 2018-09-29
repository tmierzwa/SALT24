# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0025_auto_20150404_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='crs',
            field=models.CharField(max_length=20, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assignment',
            name='from_hours',
            field=models.DecimalField(decimal_places=1, max_digits=6),
            preserve_default=True,
        ),
    ]
