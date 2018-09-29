# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ato', '0023_exercise_flight_operation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instructor',
            old_name='user',
            new_name='fbouser',
        ),
    ]
