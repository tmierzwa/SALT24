# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0033_auto_20160403_1945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='duty',
            name='my_duty_time',
        ),
    ]
