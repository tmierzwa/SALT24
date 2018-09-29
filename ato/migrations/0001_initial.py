# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Excercise',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('code', models.CharField(max_length=10, verbose_name='Kod ćwiczenia')),
                ('name', models.CharField(max_length=100, verbose_name='Nazwa ćwiczenia')),
                ('description', models.CharField(null=True, blank=True, max_length=400, verbose_name='Opis ćwiczenia')),
                ('restrictions', models.BooleanField(default=False, verbose_name='Restrykcje na instruktora')),
                ('min_h_instr', models.DecimalField(null=True, blank=True, decimal_places=1, max_digits=3, verbose_name='Min. liczba godzin z instr.')),
                ('min_h_solo', models.DecimalField(null=True, blank=True, decimal_places=1, max_digits=3, verbose_name='Min. liczba godzin solo')),
                ('min_num_instr', models.DecimalField(null=True, blank=True, decimal_places=1, max_digits=3, verbose_name='Min. liczba powtórzeń z instr.')),
                ('min_num_solo', models.DecimalField(null=True, blank=True, decimal_places=1, max_digits=3, verbose_name='Min. liczba powtórzeń solo')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('module', models.BooleanField()),
            ],
            options={
                'permissions': (('access_module', 'Dostęp do modułu szkoleń'),),
            },
        ),
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('code', models.CharField(max_length=10, verbose_name='Kod zadania/fazy')),
                ('name', models.CharField(max_length=100, verbose_name='Nazwa zadania/fazy')),
                ('description', models.CharField(null=True, blank=True, max_length=400, verbose_name='Opis zadania/fazy')),
                ('min_h_instr', models.DecimalField(null=True, blank=True, decimal_places=1, max_digits=3, verbose_name='Min. liczba godzin z instr.')),
                ('min_h_solo', models.DecimalField(null=True, blank=True, decimal_places=1, max_digits=3, verbose_name='Min. liczba godzin solo')),
                ('predecessor', models.ForeignKey(blank=True, verbose_name='Wymagane poprzednie zdanie/faza', null=True, to='ato.Phase')),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('code', models.CharField(max_length=10, verbose_name='Kod szkolenia')),
                ('name', models.CharField(max_length=100, verbose_name='Nazwa szkolenia')),
                ('description', models.CharField(null=True, blank=True, max_length=400, verbose_name='Opis szkolenia')),
            ],
        ),
        migrations.AddField(
            model_name='phase',
            name='training',
            field=models.ForeignKey(to='ato.Training', verbose_name='Szkolenie'),
        ),
        migrations.AddField(
            model_name='excercise',
            name='phase',
            field=models.ForeignKey(to='ato.Phase', verbose_name='Zadanie/faza'),
        ),
        migrations.AddField(
            model_name='excercise',
            name='predecessor',
            field=models.ForeignKey(blank=True, verbose_name='Wymagane poprzednie ćwiczenie', null=True, to='ato.Excercise'),
        ),
    ]
