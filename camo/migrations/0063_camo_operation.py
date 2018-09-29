# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0018_auto_20150813_1851'),
        ('camo', '0062_auto_20150817_1949'),
    ]

    operations = [
        migrations.CreateModel(
            name='CAMO_operation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('date', models.DateField(verbose_name='Data operacji')),
                ('tth_start', models.DecimalField(max_digits=6, decimal_places=1, verbose_name='Licznik początkowy')),
                ('tth_end', models.DecimalField(max_digits=6, decimal_places=1, verbose_name='Licznik końcowy')),
                ('landings', models.IntegerField(verbose_name='Liczba lądowań')),
                ('remarks', models.CharField(max_length=350, blank=True, verbose_name='Uwagi', null=True)),
                ('aircraft', models.ForeignKey(to='camo.Aircraft')),
                ('pdt_operation', models.ForeignKey(null=True, to='pdt.Operation', blank=True)),
            ],
        ),
    ]
