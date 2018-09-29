# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0021_auto_20150403_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pot_event',
            name='name',
            field=models.CharField(max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pot_group',
            name='name',
            field=models.CharField(max_length=500),
            preserve_default=True,
        ),
    ]
