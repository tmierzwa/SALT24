# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0010_auto_20150330_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pot_group',
            name='aircraft',
        ),
        migrations.AddField(
            model_name='pot_group',
            name='part',
            field=models.ForeignKey(default=1, to='camo.Part'),
            preserve_default=False,
        ),
    ]
