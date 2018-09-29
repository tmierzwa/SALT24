# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0075_pot_group_adsb_related'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modification',
            name='aso',
            field=models.CharField(max_length=100, verbose_name='Organizacja'),
        ),
    ]
