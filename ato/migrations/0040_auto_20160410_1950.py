# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ato', '0039_auto_20160405_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise_inst',
            name='exercise',
        ),
        migrations.RemoveField(
            model_name='phase_inst',
            name='phase',
        ),
        migrations.AddField(
            model_name='exercise_inst',
            name='code',
            field=models.CharField(default='', verbose_name='Kod ćwiczenia', max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exercise_inst',
            name='description',
            field=models.TextField(null=True, verbose_name='Opis ćwiczenia', blank=True),
        ),
        migrations.AddField(
            model_name='exercise_inst',
            name='name',
            field=models.CharField(default='', verbose_name='Nazwa ćwiczenia', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exercise_inst',
            name='restrictions',
            field=models.CharField(default='NIE', verbose_name='Restrykcje na instruktora', choices=[('TAK', 'TAK'), ('NIE', 'NIE')], max_length=3),
        ),
        migrations.AddField(
            model_name='phase_inst',
            name='code',
            field=models.CharField(default='', verbose_name='Kod zadania/fazy', max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phase_inst',
            name='description',
            field=models.TextField(null=True, verbose_name='Opis zadania/fazy', blank=True),
        ),
        migrations.AddField(
            model_name='phase_inst',
            name='name',
            field=models.CharField(default='', verbose_name='Nazwa zadania/fazy', max_length=120),
            preserve_default=False,
        ),
    ]
