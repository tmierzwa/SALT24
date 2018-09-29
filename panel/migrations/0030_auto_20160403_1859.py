# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import timedelta
from django.db import models, migrations
import panel.models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0029_auto_20160324_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='duty',
            name='my_duty_time',
            field=panel.models.MyDurationField(default=timedelta(seconds=0), verbose_name='Czas pracy'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='duty',
            name='duty_time',
            field=models.DurationField(verbose_name='Stary czas pracy'),
        ),
    ]
