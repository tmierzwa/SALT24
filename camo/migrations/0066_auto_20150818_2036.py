# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0065_camo_operation_pdt_ref'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aircraft',
            options={'permissions': (('view_aircraft', 'Może przeglądać SP'),)},
        ),
    ]
