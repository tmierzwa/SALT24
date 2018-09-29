# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pilot',
            name='upowaznienie',
            field=models.CharField(blank=True, null=True, verbose_name='Numer upowa?nienia', max_length=100),
            preserve_default=True,
        ),
    ]
