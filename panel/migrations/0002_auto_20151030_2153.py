# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fbouser',
            name='employee',
            field=models.BooleanField(verbose_name='Pracownik', default=False),
        ),
        migrations.AlterField(
            model_name='fbouser',
            name='restrictions',
            field=models.BooleanField(verbose_name='Restrykcje', default=False),
        ),
    ]
