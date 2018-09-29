# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0020_auto_20160324_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='smsreport',
            name='privacy',
            field=models.BooleanField(verbose_name='Proszę o zachowanie poufnosci', default=False),
        ),
    ]
