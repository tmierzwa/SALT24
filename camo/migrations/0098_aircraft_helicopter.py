# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0097_auto_20160324_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='aircraft',
            name='helicopter',
            field=models.BooleanField(default=False, verbose_name='Czy śmigłowiec'),
        ),
    ]
