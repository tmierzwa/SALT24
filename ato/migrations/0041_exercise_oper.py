# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import salt.models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0034_remove_duty_my_duty_time'),
        ('ato', '0040_auto_20160410_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise_oper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('solo', models.BooleanField(verbose_name='Lot solo', default=False)),
                ('time_allocated', salt.models.MyDurationField(verbose_name='Czas ćwiczenia', default=datetime.timedelta(0))),
                ('num_allocated', models.IntegerField(verbose_name='Liczba powtórzeń ćwiczenia', default=0)),
                ('remarks', models.TextField(verbose_name='Uwagi', null=True, blank=True)),
                ('exercise_inst', models.ForeignKey(verbose_name='Cwiczenie', to='ato.Exercise_inst')),
                ('operation', models.ForeignKey(verbose_name='Operacja', to='panel.Operation')),
            ],
        ),
    ]
