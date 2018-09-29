# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0083_auto_20160106_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraft',
            name='type',
            field=models.CharField(verbose_name='Typ SP', max_length=50),
        ),
    ]
