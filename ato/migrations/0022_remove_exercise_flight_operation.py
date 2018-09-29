# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ato', '0021_auto_20160114_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise_flight',
            name='operation',
        ),
    ]
