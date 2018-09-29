# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0014_auto_20150331_1230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aircraft',
            name='months_count',
        ),
        migrations.RemoveField(
            model_name='aircraft',
            name='serial_no',
        ),
    ]
