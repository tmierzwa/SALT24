# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0014_auto_20150728_1249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='duty',
            name='pracownik',
        ),
        migrations.AlterField(
            model_name='duty',
            name='role',
            field=models.CharField(blank=True, verbose_name='Stanowisko', max_length=50, null=True),
            preserve_default=True,
        ),
    ]
