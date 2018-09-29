# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0061_auto_20150811_2020'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pot_group',
            options={'verbose_name_plural': 'Grupy POT'},
        ),
    ]
