# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fin', '0003_auto_20160109_1121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('voucher_id', models.CharField(max_length=20, verbose_name='Identyfikator')),
                ('voucher_code', models.CharField(max_length=10, verbose_name='Kod vouchera')),
                ('persons', models.IntegerField(verbose_name='Liczba osób')),
                ('time', models.IntegerField(verbose_name='Czas trwania (min)')),
                ('description', models.CharField(max_length=100, verbose_name='Opis vouchera')),
                ('issue_date', models.DateField(verbose_name='Data sprzedaży')),
                ('valid_date', models.DateField(verbose_name='Data ważności')),
                ('payment', models.CharField(choices=[('cash', 'Gotówka'), ('transfer', 'Przelew bankowy'), ('epay', 'Płatność elektroniczna')], max_length=10, verbose_name='Forma płatności')),
                ('paid', models.BooleanField(default=False, verbose_name='Opłacony')),
                ('done_date', models.DateField(blank=True, null=True, verbose_name='Data realizacji')),
                ('remarks', models.TextField(blank=True, null=True, verbose_name='Uwagi')),
            ],
        ),
    ]
