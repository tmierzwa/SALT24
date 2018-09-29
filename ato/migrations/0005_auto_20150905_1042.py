# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ato', '0004_auto_20150905_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='predecessor',
            field=models.ForeignKey(null=True, blank=True, verbose_name='Wymagane poprzednie ćwiczenie', on_delete=django.db.models.deletion.SET_NULL, to='ato.Exercise'),
        ),
        migrations.AlterField(
            model_name='phase',
            name='predecessor',
            field=models.ForeignKey(null=True, blank=True, verbose_name='Wymagane poprzednie zdanie/faza', on_delete=django.db.models.deletion.SET_NULL, to='ato.Phase'),
        ),
    ]
