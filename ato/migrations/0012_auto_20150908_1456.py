# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ato', '0011_auto_20150908_1316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phase_inst',
            name='h_instr',
        ),
        migrations.RemoveField(
            model_name='phase_inst',
            name='h_solo',
        ),
    ]
