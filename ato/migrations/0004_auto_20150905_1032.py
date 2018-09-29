# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ato', '0003_auto_20150905_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='min_num_instr',
            field=models.IntegerField(blank=True, null=True, verbose_name='Min. liczba powtórzeń z instr.'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='min_num_solo',
            field=models.IntegerField(blank=True, null=True, verbose_name='Min. liczba powtórzeń solo'),
        ),
    ]
