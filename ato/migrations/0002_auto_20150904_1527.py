# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ato', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=10, verbose_name='Kod ćwiczenia')),
                ('name', models.CharField(max_length=100, verbose_name='Nazwa ćwiczenia')),
                ('description', models.CharField(max_length=400, verbose_name='Opis ćwiczenia', null=True, blank=True)),
                ('restrictions', models.BooleanField(verbose_name='Restrykcje na instruktora', default=False)),
                ('min_h_instr', models.DecimalField(verbose_name='Min. liczba godzin z instr.', null=True, decimal_places=1, blank=True, max_digits=3)),
                ('min_h_solo', models.DecimalField(verbose_name='Min. liczba godzin solo', null=True, decimal_places=1, blank=True, max_digits=3)),
                ('min_num_instr', models.DecimalField(verbose_name='Min. liczba powtórzeń z instr.', null=True, decimal_places=1, blank=True, max_digits=3)),
                ('min_num_solo', models.DecimalField(verbose_name='Min. liczba powtórzeń solo', null=True, decimal_places=1, blank=True, max_digits=3)),
                ('phase', models.ForeignKey(to='ato.Phase', verbose_name='Zadanie/faza')),
                ('predecessor', models.ForeignKey(null=True, verbose_name='Wymagane poprzednie ćwiczenie', to='ato.Exercise', blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='excercise',
            name='phase',
        ),
        migrations.RemoveField(
            model_name='excercise',
            name='predecessor',
        ),
        migrations.DeleteModel(
            name='Excercise',
        ),
    ]
