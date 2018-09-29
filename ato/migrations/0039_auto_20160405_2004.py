# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ato', '0038_auto_20160405_2001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise',
            old_name='new_min_time_instr',
            new_name='min_time_instr',
        ),
        migrations.RenameField(
            model_name='exercise',
            old_name='new_min_time_solo',
            new_name='min_time_solo',
        ),
        migrations.RenameField(
            model_name='exercise_inst',
            old_name='new_min_time_instr',
            new_name='min_time_instr',
        ),
        migrations.RenameField(
            model_name='exercise_inst',
            old_name='new_min_time_solo',
            new_name='min_time_solo',
        ),
        migrations.RenameField(
            model_name='exercise_inst',
            old_name='new_time_instr',
            new_name='time_instr',
        ),
        migrations.RenameField(
            model_name='exercise_inst',
            old_name='new_time_solo',
            new_name='time_solo',
        ),
        migrations.RenameField(
            model_name='phase',
            old_name='new_min_time_instr',
            new_name='min_time_instr',
        ),
        migrations.RenameField(
            model_name='phase',
            old_name='new_min_time_solo',
            new_name='min_time_solo',
        ),
        migrations.RenameField(
            model_name='phase_inst',
            old_name='new_min_time_instr',
            new_name='min_time_instr',
        ),
        migrations.RenameField(
            model_name='phase_inst',
            old_name='new_min_time_solo',
            new_name='min_time_solo',
        ),
    ]
