# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0081_auto_20151122_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='pot_group',
            name='applies',
            field=models.BooleanField(default=True, verbose_name='Dotyczy danej części'),
        ),
    ]
