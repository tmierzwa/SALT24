# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ato', '0008_auto_20150908_1129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise_inst',
            name='description',
        ),
        migrations.RemoveField(
            model_name='phase_inst',
            name='description',
        ),
        migrations.RemoveField(
            model_name='training_inst',
            name='description',
        ),
    ]
