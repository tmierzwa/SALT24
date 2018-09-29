# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ato', '0034_auto_20160317_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise_flight',
            name='exercise_inst',
        ),
        migrations.RemoveField(
            model_name='exercise_flight',
            name='operation',
        ),
        migrations.AlterField(
            model_name='training_inst',
            name='passed',
            field=models.CharField(choices=[('TAK', 'TAK'), ('NIE', 'NIE')], verbose_name='Ukończone', max_length=3, default='NIE'),
        ),
        migrations.DeleteModel(
            name='Exercise_flight',
        ),
    ]
