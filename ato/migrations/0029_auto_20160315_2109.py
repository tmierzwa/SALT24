# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ato', '0028_auto_20160315_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phase',
            name='min_time_instr',
            field=models.TimeField(null=True, blank=True, verbose_name='Min. czas z instr.'),
        ),
        migrations.AlterField(
            model_name='phase',
            name='min_time_solo',
            field=models.TimeField(null=True, blank=True, verbose_name='Min. czas solo'),
        ),
    ]
