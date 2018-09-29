# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fin', '0004_voucher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contractor_id', models.CharField(verbose_name='Identyfikator FK', max_length=20)),
                ('name', models.CharField(verbose_name='Nazwa kontrahenta', max_length=100)),
                ('address1', models.CharField(verbose_name='Adres kontrahenta', max_length=100)),
                ('address2', models.CharField(verbose_name='Adres kontrahenta', max_length=100)),
                ('company', models.BooleanField(verbose_name='Firma', default=False)),
                ('pesel', models.CharField(verbose_name='Numer PESEL', null=True, max_length=11, blank=True)),
                ('nip', models.CharField(verbose_name='Numer NIP', null=True, max_length=15, blank=True)),
                ('regon', models.CharField(verbose_name='Numer REGON', null=True, max_length=9, blank=True)),
                ('active', models.BooleanField(verbose_name='Czy aktywny?', default=True)),
                ('ato_balance', models.DecimalField(verbose_name='Saldo szkoleń', max_digits=7, decimal_places=2, default=0)),
                ('rent_balance', models.DecimalField(verbose_name='Saldo wynajmu', max_digits=7, decimal_places=2, default=0)),
                ('aoc_balance', models.DecimalField(verbose_name='Saldo AOC', max_digits=7, decimal_places=2, default=0)),
                ('spo_balance', models.DecimalField(verbose_name='Saldo usług', max_digits=7, decimal_places=2, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='RentPackage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('package_id', models.CharField(verbose_name='Identyfikator pakietu', max_length=20)),
                ('name', models.CharField(verbose_name='Nazwa pakietu', max_length=100)),
                ('ac_type', models.CharField(verbose_name='Typ SP', max_length=50)),
                ('hours', models.IntegerField(verbose_name='Liczba godzin')),
                ('hour_price', models.DecimalField(verbose_name='Cena za godzinę', max_digits=6, decimal_places=2)),
                ('remarks', models.TextField(verbose_name='Uwagi', null=True, blank=True)),
            ],
        ),
    ]
