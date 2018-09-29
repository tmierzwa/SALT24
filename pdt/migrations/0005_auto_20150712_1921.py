# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0004_auto_20150712_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdt',
            name='sic',
            field=models.ForeignKey(blank=True, null=True, to='pdt.Pilot', related_name='pdt_sic_set'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pdt',
            name='status',
            field=models.CharField(default='open', blank=True, choices=[('open', 'Otwarty'), ('closed', 'Zamkni?ty')], null=True, max_length=10, verbose_name='Status'),
            preserve_default=True,
        ),
    ]
