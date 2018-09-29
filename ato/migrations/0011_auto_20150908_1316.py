# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ato', '0010_auto_20150908_1307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise_flight',
            old_name='excercise_inst',
            new_name='exercise_inst',
        ),
    ]
