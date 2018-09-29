# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0018_auto_20150813_1851'),
        ('ato', '0007_instructor_license'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise_flight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('h_instr', models.DecimalField(blank=True, verbose_name='Liczba godzin z instr.', decimal_places=1, max_digits=3, null=True)),
                ('h_solo', models.DecimalField(blank=True, verbose_name='Liczba godzin solo', decimal_places=1, max_digits=3, null=True)),
                ('landings', models.IntegerField(blank=True, verbose_name='Liczba lądowań', null=True)),
                ('remarks', models.CharField(blank=True, verbose_name='Uwagi', max_length=400, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise_inst',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(blank=True, verbose_name='Opis ćwiczenia', max_length=400, null=True)),
                ('min_h_instr', models.DecimalField(blank=True, verbose_name='Min. liczba godzin z instr.', decimal_places=1, max_digits=3, null=True)),
                ('min_h_solo', models.DecimalField(blank=True, verbose_name='Min. liczba godzin solo', decimal_places=1, max_digits=3, null=True)),
                ('min_num_instr', models.IntegerField(blank=True, verbose_name='Min. liczba powtórzeń z instr.', null=True)),
                ('min_num_solo', models.IntegerField(blank=True, verbose_name='Min. liczba powtórzeń solo', null=True)),
                ('h_instr', models.DecimalField(verbose_name='Liczba godzin z instr.', decimal_places=1, max_digits=3, default=0)),
                ('h_solo', models.DecimalField(verbose_name='Liczba godzin solo', decimal_places=1, max_digits=3, default=0)),
                ('num_instr', models.IntegerField(verbose_name='Liczba powtórzeń z instr.', default=0)),
                ('num_solo', models.IntegerField(verbose_name='Liczba powtórzeń solo', default=0)),
                ('passed', models.CharField(verbose_name='Zaliczenie', max_length=3, choices=[('TAK', 'TAK'), ('NIE', 'NIE')], default='NIE')),
                ('remarks', models.CharField(blank=True, verbose_name='Uwagi', max_length=400, null=True)),
                ('excercise', models.ForeignKey(verbose_name='Cwiczenie', to='ato.Exercise')),
            ],
        ),
        migrations.CreateModel(
            name='Phase_inst',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(blank=True, verbose_name='Opis zadania/fazy', max_length=400, null=True)),
                ('min_h_instr', models.DecimalField(blank=True, verbose_name='Min. liczba godzin z instr.', decimal_places=1, max_digits=3, null=True)),
                ('min_h_solo', models.DecimalField(blank=True, verbose_name='Min. liczba godzin solo', decimal_places=1, max_digits=3, null=True)),
                ('h_instr', models.DecimalField(verbose_name='Liczba godzin z instr.', decimal_places=1, max_digits=3, default=0)),
                ('h_solo', models.DecimalField(verbose_name='Liczba godzin solo', decimal_places=1, max_digits=3, default=0)),
                ('passed', models.CharField(verbose_name='Zaliczenie', max_length=3, choices=[('TAK', 'TAK'), ('NIE', 'NIE')], default='NIE')),
                ('remarks', models.CharField(blank=True, verbose_name='Uwagi', max_length=400, null=True)),
                ('phase', models.ForeignKey(verbose_name='Zadanie/faza', to='ato.Phase')),
                ('predecessor', models.ForeignKey(to='ato.Phase_inst', null=True, blank=True, verbose_name='Wymagane poprzednie zdanie/faza', on_delete=django.db.models.deletion.SET_NULL)),
            ],
        ),
        migrations.CreateModel(
            name='Training_inst',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(blank=True, verbose_name='Opis szkolenia', max_length=400, null=True)),
                ('start_date', models.DateField(verbose_name='Data rozpoczęcia')),
                ('passed', models.CharField(verbose_name='Zaliczenie', max_length=3, choices=[('TAK', 'TAK'), ('NIE', 'NIE')], default='NIE')),
                ('pass_date', models.DateField(blank=True, verbose_name='Data ukończenia', null=True)),
                ('open', models.BooleanField(verbose_name='Czy otwarte', default=True)),
                ('remarks', models.CharField(blank=True, verbose_name='Uwagi', max_length=400, null=True)),
                ('instructor', models.ForeignKey(verbose_name='Instruktor prowadzący', to='ato.Instructor')),
                ('student', models.ForeignKey(verbose_name='Student', to='ato.Student')),
                ('training', models.ForeignKey(verbose_name='Szkolenie', to='ato.Training')),
            ],
        ),
        migrations.AddField(
            model_name='phase_inst',
            name='training_inst',
            field=models.ForeignKey(verbose_name='Szkolenie', to='ato.Training_inst'),
        ),
        migrations.AddField(
            model_name='exercise_inst',
            name='phase_inst',
            field=models.ForeignKey(verbose_name='Zadanie/faza', to='ato.Phase_inst'),
        ),
        migrations.AddField(
            model_name='exercise_inst',
            name='predecessor',
            field=models.ForeignKey(to='ato.Exercise_inst', null=True, blank=True, verbose_name='Wymagane poprzednie ćwiczenie', on_delete=django.db.models.deletion.SET_NULL),
        ),
        migrations.AddField(
            model_name='exercise_flight',
            name='excercise_inst',
            field=models.ForeignKey(verbose_name='Cwiczenie', to='ato.Exercise_inst'),
        ),
        migrations.AddField(
            model_name='exercise_flight',
            name='operation',
            field=models.ForeignKey(verbose_name='Operacja z PDT', to='pdt.Operation'),
        ),
    ]
