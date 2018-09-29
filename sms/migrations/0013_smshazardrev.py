# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0012_auto_20150904_1149'),
    ]

    operations = [
        migrations.CreateModel(
            name='SMSHazardRev',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('rev_num', models.IntegerField(default=1, verbose_name='Numer wersji')),
                ('rev_date', models.DateField(verbose_name='Data wersji')),
                ('rev_last', models.BooleanField(default=True, verbose_name='Aktualna wersja')),
                ('company_area', models.CharField(max_length=10, choices=[('SALT', 'SALT'), ('ATO', 'ATO'), ('AOC', 'AOC'), ('Inne', 'Inne')], verbose_name='Obszar firmy')),
                ('name', models.CharField(max_length=200, verbose_name='Nazwa zagrożenia')),
                ('due_date', models.DateField(null=True, blank=True, verbose_name='Termin')),
                ('responsible', models.CharField(null=True, max_length=50, blank=True, verbose_name='Osoba odpowiedzialna')),
                ('control', models.CharField(null=True, max_length=100, blank=True, verbose_name='Wykonanie / kontrola')),
                ('remarks', models.CharField(null=True, max_length=1000, blank=True, verbose_name='Uwagi')),
                ('hazard', models.ForeignKey(to='sms.SMSHazard', verbose_name='Zarejestrowane zagrożenie')),
            ],
        ),
    ]
