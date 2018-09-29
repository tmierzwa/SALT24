# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ato', '0030_auto_20160316_0813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='min_h_instr',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='min_h_solo',
        ),
        migrations.RemoveField(
            model_name='exercise_inst',
            name='h_instr',
        ),
        migrations.RemoveField(
            model_name='exercise_inst',
            name='h_solo',
        ),
        migrations.RemoveField(
            model_name='exercise_inst',
            name='min_h_instr',
        ),
        migrations.RemoveField(
            model_name='exercise_inst',
            name='min_h_solo',
        ),
        migrations.RemoveField(
            model_name='phase',
            name='min_h_instr',
        ),
        migrations.RemoveField(
            model_name='phase',
            name='min_h_solo',
        ),
        migrations.RemoveField(
            model_name='phase_inst',
            name='min_h_instr',
        ),
        migrations.RemoveField(
            model_name='phase_inst',
            name='min_h_solo',
        ),
    ]
