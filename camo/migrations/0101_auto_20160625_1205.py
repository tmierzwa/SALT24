# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0100_auto_20160625_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ms_report',
            name='crs_date',
            field=models.CharField(blank=True, null=True, max_length=21, verbose_name='Data CRS'),
        ),
    ]
