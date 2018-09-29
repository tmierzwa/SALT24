# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ato', '0033_training_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='name',
            field=models.CharField(verbose_name='Nazwa ćwiczenia', max_length=150),
        ),
        migrations.AlterField(
            model_name='training',
            name='name',
            field=models.CharField(verbose_name='Nazwa szkolenia', max_length=100),
        ),
    ]
