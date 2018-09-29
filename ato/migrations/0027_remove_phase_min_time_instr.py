# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ato', '0026_phase_min_time_instr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phase',
            name='min_time_instr',
        ),
    ]
