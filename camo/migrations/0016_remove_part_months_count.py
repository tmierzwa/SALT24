# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0015_auto_20150331_1853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='part',
            name='months_count',
        ),
    ]
