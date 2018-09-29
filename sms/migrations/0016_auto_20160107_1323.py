# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0015_auto_20151230_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smshazardrev',
            name='due_date',
            field=models.CharField(verbose_name='Termin wykonania', null=True, blank=True, max_length=30),
        ),
    ]
