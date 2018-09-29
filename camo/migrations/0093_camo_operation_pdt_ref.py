# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0092_auto_20160222_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='camo_operation',
            name='pdt_ref',
            field=models.CharField(blank=True, null=True, max_length=20, verbose_name='Numer PDT'),
        ),
    ]
