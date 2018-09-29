# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0067_auto_20150818_2041'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pot_group',
            options={},
        ),
        migrations.AlterField(
            model_name='camo_operation',
            name='pdt_ref',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Numer PDT'),
        ),
    ]
