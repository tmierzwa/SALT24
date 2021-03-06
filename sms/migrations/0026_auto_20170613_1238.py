# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-13 10:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0025_auto_20170115_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smsevent',
            name='description',
            field=models.TextField(verbose_name='Opis zdarzenia'),
        ),
        migrations.AlterField(
            model_name='smsevent',
            name='findings',
            field=models.TextField(blank=True, null=True, verbose_name='Wnioski i zalecenia po badaniu wewnętrznym'),
        ),
        migrations.AlterField(
            model_name='smsevent',
            name='remarks',
            field=models.TextField(blank=True, null=True, verbose_name='Uwagi'),
        ),
        migrations.AlterField(
            model_name='smsevent',
            name='scrutiny',
            field=models.TextField(blank=True, null=True, verbose_name='Przebieg badania wewnętrznego'),
        ),
        migrations.AlterField(
            model_name='smsfailure',
            name='description',
            field=models.TextField(verbose_name='Opis usterki'),
        ),
        migrations.AlterField(
            model_name='smsfailure',
            name='findings',
            field=models.TextField(blank=True, null=True, verbose_name='Wnioski i zalecenia ogólne'),
        ),
        migrations.AlterField(
            model_name='smshazardrev',
            name='control',
            field=models.TextField(blank=True, null=True, verbose_name='Wykonanie / kontrola'),
        ),
        migrations.AlterField(
            model_name='smshazardrev',
            name='remarks',
            field=models.TextField(blank=True, null=True, verbose_name='Uwagi'),
        ),
        migrations.AlterField(
            model_name='smsreport',
            name='description',
            field=models.TextField(verbose_name='Treść zgłoszenia'),
        ),
        migrations.AlterField(
            model_name='smsreport',
            name='findings',
            field=models.TextField(blank=True, null=True, verbose_name='Wnioski i zalecenia'),
        ),
        migrations.AlterField(
            model_name='smsreport',
            name='remarks',
            field=models.TextField(blank=True, null=True, verbose_name='Uwagi'),
        ),
        migrations.AlterField(
            model_name='smsrisk',
            name='description',
            field=models.TextField(verbose_name='Szczegółowy opis natury ryzyka'),
        ),
        migrations.AlterField(
            model_name='smsrisk',
            name='mitigation',
            field=models.TextField(blank=True, null=True, verbose_name='Sposoby ograniczania ryzyka'),
        ),
    ]
