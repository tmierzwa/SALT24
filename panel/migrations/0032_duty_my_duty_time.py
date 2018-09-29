# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from datetime import timedelta


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0031_remove_duty_my_duty_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='duty',
            name='my_duty_time',
            field=models.DurationField(default=timedelta(seconds=0), verbose_name='Czas pracy'),
            preserve_default=False,
        ),
    ]
