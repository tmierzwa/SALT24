# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0063_camo_operation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camo_operation',
            name='pdt_operation',
            field=models.OneToOneField(blank=True, null=True, to='pdt.Operation'),
        ),
    ]
