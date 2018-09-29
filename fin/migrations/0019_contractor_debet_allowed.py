# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fin', '0018_auto_20160324_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractor',
            name='debet_allowed',
            field=models.BooleanField(default=False, verbose_name='Zgoda na debet'),
        ),
    ]
