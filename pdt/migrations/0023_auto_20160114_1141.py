# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fin', '0011_auto_20160114_1141'),
        ('camo', '0085_auto_20160114_1141'),
        ('ato', '0020_auto_20160114_1141'),
        ('sms', '0017_auto_20160114_1141'),
        ('pdt', '0022_delete_voucher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='duty',
            name='pilot',
        ),
        migrations.RemoveField(
            model_name='operation',
            name='pdt',
        ),
        migrations.RemoveField(
            model_name='pdt',
            name='aircraft',
        ),
        migrations.RemoveField(
            model_name='pdt',
            name='instr',
        ),
        migrations.RemoveField(
            model_name='pdt',
            name='pic',
        ),
        migrations.RemoveField(
            model_name='pdt',
            name='sic',
        ),
        migrations.DeleteModel(
            name='Duty',
        ),
        migrations.DeleteModel(
            name='Operation',
        ),
        migrations.DeleteModel(
            name='PDT',
        ),
        migrations.DeleteModel(
            name='Pilot',
        ),
    ]
