# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0035_auto_20150408_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pot_event',
            name='name',
            field=models.CharField(max_length=800),
            preserve_default=True,
        ),
    ]
