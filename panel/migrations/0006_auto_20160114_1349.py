# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0005_auto_20160114_1141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pilot',
            old_name='clereance',
            new_name='clearance',
        ),
    ]
