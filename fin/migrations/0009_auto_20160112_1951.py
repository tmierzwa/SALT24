# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fin', '0008_auto_20160112_1738'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoldPackage',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('package_id', models.CharField(max_length=20, verbose_name='Identyfikator pakietu')),
                ('name', models.CharField(max_length=100, verbose_name='Nazwa pakietu')),
                ('ac_type', models.CharField(max_length=50, verbose_name='Typ SP')),
                ('hours', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Liczba godzin')),
                ('left_hours', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Pozostała liczba godzin')),
                ('hour_price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Cena za godzinę')),
                ('remarks', models.TextField(null=True, blank=True, verbose_name='Uwagi')),
                ('contractor', models.ForeignKey(to='fin.Contractor', verbose_name='Kontrahent')),
            ],
        ),
        migrations.CreateModel(
            name='SpecialPrice',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('ac_type', models.CharField(max_length=50, verbose_name='Typ SP')),
                ('hour_price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Cena za godzinę')),
                ('remarks', models.TextField(null=True, blank=True, verbose_name='Uwagi')),
                ('contractor', models.ForeignKey(to='fin.Contractor', verbose_name='Kontrahent')),
            ],
        ),
        migrations.AlterField(
            model_name='balanceoperation',
            name='aoc_amount',
            field=models.DecimalField(decimal_places=2, max_digits=8, default=0, verbose_name='Kwota operacji (AOC)'),
        ),
        migrations.AlterField(
            model_name='balanceoperation',
            name='ato_amount',
            field=models.DecimalField(decimal_places=2, max_digits=8, default=0, verbose_name='Kwota operacji (szkolenia)'),
        ),
        migrations.AlterField(
            model_name='balanceoperation',
            name='rent_amount',
            field=models.DecimalField(decimal_places=2, max_digits=8, default=0, verbose_name='Kwota operacji (wynajem)'),
        ),
        migrations.AlterField(
            model_name='balanceoperation',
            name='spo_amount',
            field=models.DecimalField(decimal_places=2, max_digits=8, default=0, verbose_name='Kwota operacji (SPO)'),
        ),
    ]
