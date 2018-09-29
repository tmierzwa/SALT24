# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0070_auto_20151017_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pot_group',
            name='due_hours',
            field=models.IntegerField(verbose_name='Limit TTH', null=True, blank=True),
        ),
    ]
