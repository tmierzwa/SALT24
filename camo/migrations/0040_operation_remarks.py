# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0039_auto_20150409_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='remarks',
            field=models.CharField(verbose_name='Uwagi', blank=True, max_length=500, null=True),
            preserve_default=True,
        ),
    ]
