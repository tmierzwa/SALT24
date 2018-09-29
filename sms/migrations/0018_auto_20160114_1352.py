# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0017_auto_20160114_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smshazardrev',
            name='name',
            field=models.TextField(verbose_name='Nazwa zagrożenia'),
        ),
    ]
