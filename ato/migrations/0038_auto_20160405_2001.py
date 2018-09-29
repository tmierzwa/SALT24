# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ato', '0037_auto_20160405_1933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='min_time_instr',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='min_time_solo',
        ),
        migrations.RemoveField(
            model_name='exercise_inst',
            name='min_time_instr',
        ),
        migrations.RemoveField(
            model_name='exercise_inst',
            name='min_time_solo',
        ),
        migrations.RemoveField(
            model_name='exercise_inst',
            name='time_instr',
        ),
        migrations.RemoveField(
            model_name='exercise_inst',
            name='time_solo',
        ),
        migrations.RemoveField(
            model_name='phase',
            name='min_time_instr',
        ),
        migrations.RemoveField(
            model_name='phase',
            name='min_time_solo',
        ),
        migrations.RemoveField(
            model_name='phase_inst',
            name='min_time_instr',
        ),
        migrations.RemoveField(
            model_name='phase_inst',
            name='min_time_solo',
        ),
    ]
