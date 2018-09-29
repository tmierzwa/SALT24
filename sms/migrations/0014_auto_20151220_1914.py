# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0013_smshazardrev'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smshazard',
            name='company_area',
        ),
        migrations.RemoveField(
            model_name='smshazard',
            name='control',
        ),
        migrations.RemoveField(
            model_name='smshazard',
            name='due_date',
        ),
        migrations.RemoveField(
            model_name='smshazard',
            name='name',
        ),
        migrations.RemoveField(
            model_name='smshazard',
            name='remarks',
        ),
        migrations.RemoveField(
            model_name='smshazard',
            name='responsible',
        ),
    ]
