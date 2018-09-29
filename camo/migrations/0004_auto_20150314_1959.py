# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0003_auto_20150313_1949'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='maker_no',
            new_name='maker',
        ),
        migrations.AlterField(
            model_name='item_as_part',
            name='from_hours',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
