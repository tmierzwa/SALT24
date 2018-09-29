# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import panel.models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0032_duty_my_duty_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duty',
            name='my_duty_time',
            field=panel.models.MyDurationField(verbose_name='Czas pracy'),
        ),
    ]
