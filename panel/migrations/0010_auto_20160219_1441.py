# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0009_auto_20160219_1207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pdt',
            old_name='chect_time',
            new_name='check_time',
        ),
    ]
