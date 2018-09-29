# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0098_aircraft_helicopter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraft',
            name='helicopter',
            field=models.BooleanField(default=False, verbose_name='Śmigłowiec'),
        ),
    ]
