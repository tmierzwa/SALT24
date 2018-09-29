# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0009_pdt_instr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdt',
            name='status',
            field=models.CharField(max_length=10, verbose_name='Status', default='open', choices=[('open', 'Otwarty'), ('closed', 'Zamkni?ty'), ('checked', 'Sprawdzony')]),
            preserve_default=True,
        ),
    ]
