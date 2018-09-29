# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0019_auto_20151017_1343'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('voucher_id', models.CharField(verbose_name='Identyfikator', max_length=20)),
                ('person', models.CharField(verbose_name='Właściciel vouchera', max_length=100)),
                ('description', models.CharField(verbose_name='Rodzaj vouchera', max_length=100)),
                ('issue_date', models.DateField(verbose_name='Data sprzedaży')),
                ('valid_date', models.DateField(verbose_name='Data ważności')),
                ('payment', models.CharField(choices=[('cash', 'Gotówka'), ('transfer', 'Przelew bankowy'), ('epay', 'Płatność elektroniczna')], verbose_name='Forma płatności', max_length=10)),
                ('paid', models.BooleanField(default=False, verbose_name='Opłacony')),
                ('done_date', models.DateField(blank=True, verbose_name='Data realizacji', null=True)),
                ('remarks', models.TextField(blank=True, verbose_name='Uwagi', null=True)),
            ],
        ),
    ]
