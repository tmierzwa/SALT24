# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0072_ms_report'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ms_report',
            old_name='ms_date',
            new_name='done_date',
        ),
        migrations.RenameField(
            model_name='ms_report',
            old_name='hours',
            new_name='done_hours',
        ),
        migrations.RenameField(
            model_name='ms_report',
            old_name='landings',
            new_name='done_landings',
        ),
    ]
