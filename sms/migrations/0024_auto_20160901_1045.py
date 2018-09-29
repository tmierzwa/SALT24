# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0023_auto_20160830_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ncr',
            name='audit_scope',
            field=models.CharField(verbose_name='Obszar audytu', max_length=10, choices=[('AOC', 'AOC'), ('SPO', 'SPO'), ('CAMO', 'CAMO'), ('ATO', 'ATO')]),
        ),
    ]
