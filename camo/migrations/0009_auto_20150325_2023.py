# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0008_ata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraft',
            name='ac_type',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Ac_type',
        ),
    ]
