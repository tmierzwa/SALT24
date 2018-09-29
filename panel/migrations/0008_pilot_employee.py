# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0007_pilot_remarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='pilot',
            name='employee',
            field=models.BooleanField(default=False, verbose_name='Pracownik SALT'),
        ),
    ]
