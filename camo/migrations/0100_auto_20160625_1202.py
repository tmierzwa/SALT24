# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0099_auto_20160403_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ms_report',
            name='crs_date',
            field=models.CharField(null=True, blank=True, verbose_name='Data CRS', max_length=20),
        ),
    ]
