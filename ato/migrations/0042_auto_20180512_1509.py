# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-12 13:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import salt.models


class Migration(migrations.Migration):

    dependencies = [
        ('ato', '0041_exercise_oper'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card_entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name=b'Data lot\xc3\xb3w')),
                ('pdt_num', models.CharField(blank=True, max_length=12, null=True, verbose_name=b'Numer PDT')),
                ('dual_time', salt.models.MyDurationField(default=datetime.timedelta(0), verbose_name=b'Czas dwuster')),
                ('dual_num', models.IntegerField(default=0, verbose_name=b'Liczba powt\xc3\xb3rze\xc5\x84 dwuster')),
                ('solo_time', salt.models.MyDurationField(default=datetime.timedelta(0), verbose_name=b'Czas solo')),
                ('solo_num', models.IntegerField(default=0, verbose_name=b'Liczba powt\xc3\xb3rze\xc5\x84 solo')),
                ('passed', models.IntegerField(choices=[(0, b'Kontynuacja'), (1, b'Zaliczenie')], default=0, verbose_name=b'Zaliczenie')),
                ('remarks', models.TextField(blank=True, null=True, verbose_name=b'Uwagi')),
                ('internal_remarks', models.TextField(blank=True, null=True, verbose_name=b'Uwagi dla instruktor\xc3\xb3w')),
            ],
        ),
        migrations.AlterField(
            model_name='exercise',
            name='code',
            field=models.CharField(max_length=12, verbose_name=b'Kod \xc4\x87wiczenia'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name=b'Opis \xc4\x87wiczenia'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='min_num_instr',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Min. liczba powt\xc3\xb3rze\xc5\x84 z instr.'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='min_num_solo',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Min. liczba powt\xc3\xb3rze\xc5\x84 solo'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='name',
            field=models.CharField(max_length=150, verbose_name=b'Nazwa \xc4\x87wiczenia'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='predecessor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ato.Exercise', verbose_name=b'Wymagane poprzednie \xc4\x87wiczenie'),
        ),
        migrations.AlterField(
            model_name='exercise_inst',
            name='code',
            field=models.CharField(max_length=12, verbose_name=b'Kod \xc4\x87wiczenia'),
        ),
        migrations.AlterField(
            model_name='exercise_inst',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name=b'Opis \xc4\x87wiczenia'),
        ),
        migrations.AlterField(
            model_name='exercise_inst',
            name='min_num_instr',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Min. liczba powt\xc3\xb3rze\xc5\x84 z instr.'),
        ),
        migrations.AlterField(
            model_name='exercise_inst',
            name='min_num_solo',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Min. liczba powt\xc3\xb3rze\xc5\x84 solo'),
        ),
        migrations.AlterField(
            model_name='exercise_inst',
            name='name',
            field=models.CharField(max_length=150, verbose_name=b'Nazwa \xc4\x87wiczenia'),
        ),
        migrations.AlterField(
            model_name='exercise_inst',
            name='num_instr',
            field=models.IntegerField(default=0, verbose_name=b'Liczba powt\xc3\xb3rze\xc5\x84 z instr.'),
        ),
        migrations.AlterField(
            model_name='exercise_inst',
            name='num_solo',
            field=models.IntegerField(default=0, verbose_name=b'Liczba powt\xc3\xb3rze\xc5\x84 solo'),
        ),
        migrations.AlterField(
            model_name='exercise_inst',
            name='predecessor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ato.Exercise_inst', verbose_name=b'Wymagane poprzednie \xc4\x87wiczenie'),
        ),
        migrations.AlterField(
            model_name='exercise_oper',
            name='num_allocated',
            field=models.IntegerField(default=0, verbose_name=b'Liczba powt\xc3\xb3rze\xc5\x84 \xc4\x87wiczenia'),
        ),
        migrations.AlterField(
            model_name='exercise_oper',
            name='time_allocated',
            field=salt.models.MyDurationField(default=datetime.timedelta(0), verbose_name=b'Czas \xc4\x87wiczenia'),
        ),
        migrations.AlterField(
            model_name='training_inst',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ato.Instructor', verbose_name=b'Instruktor prowadz\xc4\x85cy'),
        ),
        migrations.AlterField(
            model_name='training_inst',
            name='pass_date',
            field=models.DateField(blank=True, null=True, verbose_name=b'Data uko\xc5\x84czenia'),
        ),
        migrations.AlterField(
            model_name='training_inst',
            name='passed',
            field=models.CharField(choices=[(b'TAK', b'TAK'), (b'NIE', b'NIE')], default=b'NIE', max_length=3, verbose_name=b'Uko\xc5\x84czone'),
        ),
        migrations.AlterField(
            model_name='training_inst',
            name='start_date',
            field=models.DateField(verbose_name=b'Data rozpocz\xc4\x99cia'),
        ),
        migrations.AddField(
            model_name='card_entry',
            name='exercise_inst',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ato.Exercise_inst', verbose_name=b'Cwiczenie'),
        ),
    ]
