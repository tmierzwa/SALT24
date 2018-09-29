# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0006_auto_20160114_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='pilot',
            name='remarks',
            field=models.TextField(blank=True, null=True, verbose_name='Uwagi'),
        ),
    ]
