# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ato', '0025_auto_20160114_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='phase',
            name='min_time_instr',
            field=models.DurationField(verbose_name='Min. czas z instr.', blank=True, null=True),
        ),
    ]
