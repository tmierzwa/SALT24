# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0089_wb_report_unit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wb_report',
            name='lat_moment',
        ),
        migrations.RemoveField(
            model_name='wb_report',
            name='lon_moment',
        ),
    ]
