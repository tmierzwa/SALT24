# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FBOUser',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('first_name', models.CharField(verbose_name='Imię', max_length=100)),
                ('second_name', models.CharField(verbose_name='Nazwisko', max_length=100)),
                ('email', models.EmailField(null=True, blank=True, verbose_name='Adres email', max_length=254)),
                ('active', models.BooleanField(default=True, verbose_name='Aktywny')),
                ('telephone', models.CharField(null=True, blank=True, verbose_name='Telefon kontaktowy', max_length=20)),
                ('address1', models.CharField(null=True, blank=True, verbose_name='Adres linia 1', max_length=100)),
                ('address2', models.CharField(null=True, blank=True, verbose_name='Adres linia 2', max_length=100)),
                ('birth_date', models.DateField(null=True, blank=True, verbose_name='Data urodzenia')),
                ('pesel', models.CharField(null=True, blank=True, verbose_name='Numer PESEL', max_length=11)),
                ('id_number', models.CharField(null=True, blank=True, verbose_name='Numer dowodu', max_length=11)),
                ('licence', models.CharField(null=True, blank=True, verbose_name='Numer licencji', max_length=50)),
                ('licence_date', models.DateField(null=True, blank=True, verbose_name='Ważność licencji')),
                ('medical', models.CharField(null=True, blank=True, verbose_name='Badania lotnicze', max_length=50)),
                ('medical_date', models.DateField(null=True, blank=True, verbose_name='Ważność badań')),
                ('clereance', models.CharField(null=True, blank=True, verbose_name='Upoważnienie SALT', max_length=100)),
                ('employee', models.BooleanField(default=False, verbose_name='Pracownik SALT')),
                ('student', models.BooleanField(default=False, verbose_name='Uczeń')),
                ('pilot', models.BooleanField(default=False, verbose_name='Pilot')),
                ('instructor', models.BooleanField(default=False, verbose_name='Instruktor')),
                ('restrictions', models.CharField(default='NIE', verbose_name='Restrykcje', max_length=3, choices=[('TAK', 'TAK'), ('NIE', 'NIE')])),
                ('module_ato', models.BooleanField(default=False, verbose_name='Moduł ATO')),
                ('module_camo', models.BooleanField(default=False, verbose_name='Moduł CAMO')),
                ('module_sms', models.BooleanField(default=False, verbose_name='Moduł SMS')),
                ('module_fin', models.BooleanField(default=False, verbose_name='Moduł finansowy')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, verbose_name='Login')),
            ],
        ),
    ]
