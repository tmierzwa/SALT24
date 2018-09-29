# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0023_auto_20150404_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='aircraft',
            name='wb_date',
            field=models.DateField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
