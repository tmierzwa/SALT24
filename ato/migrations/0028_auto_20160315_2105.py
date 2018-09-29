# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ato', '0027_remove_phase_min_time_instr'),
    ]

    operations = [
        migrations.AddField(
            model_name='phase',
            name='min_time_instr',
            field=models.DurationField(blank=True, null=True, verbose_name='Min. czas z instr.'),
        ),
        migrations.AddField(
            model_name='phase',
            name='min_time_solo',
            field=models.DurationField(blank=True, null=True, verbose_name='Min. czas solo'),
        ),
    ]
