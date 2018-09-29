# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0064_auto_20150817_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='camo_operation',
            name='pdt_ref',
            field=models.IntegerField(default=0, verbose_name='Numer PDT'),
            preserve_default=False,
        ),
    ]
