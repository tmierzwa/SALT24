# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0002_auto_20150712_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdt',
            name='pdt_ref',
            field=models.IntegerField(verbose_name='Numer PDT'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pdt',
            name='sic',
            field=models.ForeignKey(related_name='pdt_sic_set', to='pdt.Pilot'),
            preserve_default=True,
        ),
    ]
