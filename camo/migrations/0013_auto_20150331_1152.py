# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0012_remove_assignment_part_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operation',
            name='operation_time',
        ),
        migrations.AlterField(
            model_name='part',
            name='install_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
