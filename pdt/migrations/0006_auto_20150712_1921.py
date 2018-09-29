# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0005_auto_20150712_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdt',
            name='remarks',
            field=models.CharField(blank=True, verbose_name='Uwagi', max_length=350, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pdt',
            name='status',
            field=models.CharField(verbose_name='Status', choices=[('open', 'Otwarty'), ('closed', 'Zamkni?ty')], max_length=10, default='open'),
            preserve_default=True,
        ),
    ]
