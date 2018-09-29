# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0008_auto_20150715_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdt',
            name='instr',
            field=models.ForeignKey(blank=True, related_name='pdt_instr_set', null=True, verbose_name='Instruktor nadzoruj?cy', to='pdt.Pilot'),
            preserve_default=True,
        ),
    ]
