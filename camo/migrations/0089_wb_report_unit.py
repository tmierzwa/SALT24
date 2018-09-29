# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0088_aircraft_remarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='wb_report',
            name='unit',
            field=models.CharField(verbose_name='Jednostki', choices=[('EU', 'EU'), ('USA', 'USA')], max_length=3, default='EU'),
        ),
    ]
