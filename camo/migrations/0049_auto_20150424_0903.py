# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0048_auto_20150420_1144'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aso',
            options={'verbose_name_plural': 'Organizacje ASO'},
        ),
        migrations.AlterModelOptions(
            name='ata',
            options={'verbose_name_plural': 'Sekcje ATA'},
        ),
        migrations.AddField(
            model_name='part',
            name='f1',
            field=models.CharField(verbose_name='FORM-1', null=True, blank=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='part',
            name='install_date',
            field=models.DateField(verbose_name='Data pierwszej instalacji', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='work_order',
            name='date',
            field=models.DateField(default=datetime.date(2015, 4, 24)),
            preserve_default=True,
        ),
    ]
