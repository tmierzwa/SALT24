# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0087_auto_20160123_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='aircraft',
            name='remarks',
            field=models.TextField(null=True, verbose_name='Uwagi', blank=True),
        ),
    ]
