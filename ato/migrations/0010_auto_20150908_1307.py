# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ato', '0009_auto_20150908_1138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise_inst',
            old_name='excercise',
            new_name='exercise',
        ),
    ]
