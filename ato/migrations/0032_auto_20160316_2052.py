# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ato', '0031_auto_20160316_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='description',
            field=models.TextField(null=True, verbose_name='Opis ćwiczenia', blank=True),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='name',
            field=models.CharField(verbose_name='Nazwa ćwiczenia', max_length=120),
        ),
        migrations.AlterField(
            model_name='exercise_flight',
            name='remarks',
            field=models.TextField(null=True, verbose_name='Uwagi', blank=True),
        ),
        migrations.AlterField(
            model_name='exercise_inst',
            name='remarks',
            field=models.TextField(null=True, verbose_name='Uwagi', blank=True),
        ),
        migrations.AlterField(
            model_name='phase',
            name='description',
            field=models.TextField(null=True, verbose_name='Opis zadania/fazy', blank=True),
        ),
        migrations.AlterField(
            model_name='phase',
            name='name',
            field=models.CharField(verbose_name='Nazwa zadania/fazy', max_length=120),
        ),
        migrations.AlterField(
            model_name='phase_inst',
            name='remarks',
            field=models.TextField(null=True, verbose_name='Uwagi', blank=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='description',
            field=models.TextField(null=True, verbose_name='Opis szkolenia', blank=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='name',
            field=models.CharField(verbose_name='Nazwa szkolenia', max_length=120),
        ),
        migrations.AlterField(
            model_name='training_inst',
            name='remarks',
            field=models.TextField(null=True, verbose_name='Uwagi', blank=True),
        ),
    ]
