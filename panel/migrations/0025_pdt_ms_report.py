# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0096_auto_20160308_0834'),
        ('panel', '0024_auto_20160315_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdt',
            name='ms_report',
            field=models.ForeignKey(null=True, blank=True, verbose_name='Na podstawie MS', to='camo.MS_report'),
        ),
    ]
