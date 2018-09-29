# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0077_auto_20151114_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pot_group',
            name='done_aso',
            field=models.CharField(blank=True, verbose_name='Wykonano (ASO)', null=True, max_length=100),
        ),
    ]
