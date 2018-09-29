# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ato', '0029_auto_20160315_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='min_time_instr',
            field=models.TimeField(blank=True, null=True, verbose_name='Min. czas z instr.'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='min_time_solo',
            field=models.TimeField(blank=True, null=True, verbose_name='Min. czas solo'),
        ),
        migrations.AddField(
            model_name='exercise_inst',
            name='min_time_instr',
            field=models.TimeField(blank=True, null=True, verbose_name='Min. czas z instr.'),
        ),
        migrations.AddField(
            model_name='exercise_inst',
            name='min_time_solo',
            field=models.TimeField(blank=True, null=True, verbose_name='Min. czas solo'),
        ),
        migrations.AddField(
            model_name='exercise_inst',
            name='time_instr',
            field=models.TimeField(blank=True, null=True, verbose_name='Czas z instr.'),
        ),
        migrations.AddField(
            model_name='exercise_inst',
            name='time_solo',
            field=models.TimeField(blank=True, null=True, verbose_name='Czas solo'),
        ),
        migrations.AddField(
            model_name='phase_inst',
            name='min_time_instr',
            field=models.TimeField(blank=True, null=True, verbose_name='Min. czas z instr.'),
        ),
        migrations.AddField(
            model_name='phase_inst',
            name='min_time_solo',
            field=models.TimeField(blank=True, null=True, verbose_name='Min. czas solo'),
        ),
    ]
