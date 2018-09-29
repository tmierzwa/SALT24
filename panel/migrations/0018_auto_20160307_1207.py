# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0017_auto_20160305_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pdt',
            name='available_fuel',
        ),
        migrations.RemoveField(
            model_name='pdt',
            name='cycles',
        ),
        migrations.RemoveField(
            model_name='pdt',
            name='landings',
        ),
        migrations.RemoveField(
            model_name='pdt',
            name='tth_end',
        ),
    ]
