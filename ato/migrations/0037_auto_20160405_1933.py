# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import salt.models


class Migration(migrations.Migration):

    dependencies = [
        ('ato', '0036_auto_20160324_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='new_min_time_instr',
            field=salt.models.MyDurationField(null=True, blank=True, verbose_name='Min. czas z instr.'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='new_min_time_solo',
            field=salt.models.MyDurationField(null=True, blank=True, verbose_name='Min. czas solo'),
        ),
        migrations.AddField(
            model_name='exercise_inst',
            name='new_min_time_instr',
            field=salt.models.MyDurationField(null=True, blank=True, verbose_name='Min. czas z instr.'),
        ),
        migrations.AddField(
            model_name='exercise_inst',
            name='new_min_time_solo',
            field=salt.models.MyDurationField(null=True, blank=True, verbose_name='Min. czas solo'),
        ),
        migrations.AddField(
            model_name='exercise_inst',
            name='new_time_instr',
            field=salt.models.MyDurationField(null=True, blank=True, verbose_name='Czas z instr.'),
        ),
        migrations.AddField(
            model_name='exercise_inst',
            name='new_time_solo',
            field=salt.models.MyDurationField(null=True, blank=True, verbose_name='Czas solo'),
        ),
        migrations.AddField(
            model_name='phase',
            name='new_min_time_instr',
            field=salt.models.MyDurationField(null=True, blank=True, verbose_name='Min. czas z instr.'),
        ),
        migrations.AddField(
            model_name='phase',
            name='new_min_time_solo',
            field=salt.models.MyDurationField(null=True, blank=True, verbose_name='Min. czas solo'),
        ),
        migrations.AddField(
            model_name='phase_inst',
            name='new_min_time_instr',
            field=salt.models.MyDurationField(null=True, blank=True, verbose_name='Min. czas z instr.'),
        ),
        migrations.AddField(
            model_name='phase_inst',
            name='new_min_time_solo',
            field=salt.models.MyDurationField(null=True, blank=True, verbose_name='Min. czas solo'),
        ),
    ]
