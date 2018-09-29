# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0074_auto_20151113_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='pot_group',
            name='adsb_related',
            field=models.CharField(verbose_name='Powiązanie AD/SB', null=True, blank=True, max_length=50),
        ),
    ]
