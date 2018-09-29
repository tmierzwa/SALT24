# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ato', '0005_auto_20150905_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('first_name', models.CharField(verbose_name='Imię', max_length=10)),
                ('name', models.CharField(verbose_name='Nazwisko', max_length=100)),
                ('telephone', models.CharField(verbose_name='Numer telefonu', max_length=20, blank=True, null=True)),
                ('email', models.CharField(verbose_name='Adres e-mail', max_length=50, blank=True, null=True)),
                ('restrictions', models.CharField(verbose_name='Restrykcje', max_length=3, choices=[('TAK', 'TAK'), ('NIE', 'NIE')], default='NIE')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('first_name', models.CharField(verbose_name='Imię', max_length=10)),
                ('name', models.CharField(verbose_name='Nazwisko', max_length=100)),
                ('birth_date', models.DateField(verbose_name='Data urodzenia')),
                ('pesel', models.CharField(verbose_name='PESEL', max_length=11, blank=True, null=True)),
                ('telephone', models.CharField(verbose_name='Numer telefonu', max_length=20, blank=True, null=True)),
                ('email', models.CharField(verbose_name='Adres e-mail', max_length=50, blank=True, null=True)),
            ],
        ),
    ]
