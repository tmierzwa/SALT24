# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import salt.models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0037_auto_20160830_1920'),
    ]

    operations = [
        migrations.RenameField(
            model_name='duty',
            old_name='block_time_factor',
            new_name='time_factor',
        ),
        migrations.RemoveField(
            model_name='duty',
            name='block_time_from',
        ),
        migrations.RemoveField(
            model_name='duty',
            name='block_time_to',
        ),
        migrations.AddField(
            model_name='duty',
            name='fdp_time',
            field=salt.models.MyDurationField(blank=True, null=True, verbose_name='Czas czynności lotniczych'),
        ),
        migrations.AddField(
            model_name='duty',
            name='landings',
            field=models.IntegerField(blank=True, null=True, verbose_name='Liczba lądowań'),
        ),
    ]
