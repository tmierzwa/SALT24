# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0005_module'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smshazard',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nazwa zagrożenia'),
        ),
    ]
