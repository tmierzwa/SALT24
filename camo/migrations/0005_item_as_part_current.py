# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0004_auto_20150314_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='item_as_part',
            name='current',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
