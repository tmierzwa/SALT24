# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0032_auto_20150406_1043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aircraft',
            name='hours_count',
        ),
        migrations.RemoveField(
            model_name='aircraft',
            name='landings_count',
        ),
        migrations.RemoveField(
            model_name='pot_group',
            name='hours_count',
        ),
        migrations.RemoveField(
            model_name='pot_group',
            name='landings_count',
        ),
    ]
