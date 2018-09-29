# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0009_auto_20150822_2202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smsfailure',
            name='remarks',
        ),
        migrations.AddField(
            model_name='smsfailure',
            name='aircraft',
            field=models.CharField(verbose_name='Statek powietrzny', max_length=10, default='SP'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='smsfailure',
            name='crs',
            field=models.CharField(verbose_name='Numer CRS', null=True, max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='smsfailure',
            name='event_date',
            field=models.DateField(verbose_name='Data usterki', default=datetime.datetime(2015, 8, 24, 18, 39, 16, 791015, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='smsfailure',
            name='person',
            field=models.CharField(verbose_name='Osoba zgłaszająca', null=True, max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='smsfailure',
            name='description',
            field=models.CharField(max_length=500, verbose_name='Opis usterki'),
        ),
        migrations.AlterField(
            model_name='smsfailure',
            name='findings',
            field=models.CharField(verbose_name='Wnioski i zalecenia ogólne', null=True, max_length=500, blank=True),
        ),
        migrations.AlterField(
            model_name='smsfailure',
            name='pdt_ref',
            field=models.ForeignKey(null=True, to='pdt.PDT', verbose_name='Numer PDT', blank=True),
        ),
    ]
