# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0014_auto_20151220_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='smsrisk',
            name='rev_date',
            field=models.DateField(default=datetime.datetime(2015, 12, 30, 9, 53, 48, 661809, tzinfo=utc), verbose_name='Data wersji'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='smsrisk',
            name='rev_last',
            field=models.BooleanField(default=True, verbose_name='Aktualna wersja'),
        ),
        migrations.AddField(
            model_name='smsrisk',
            name='rev_num',
            field=models.IntegerField(default=1, verbose_name='Numer wersji'),
        ),
        migrations.AddField(
            model_name='smsrisk',
            name='risk_ref',
            field=models.CharField(default='-', verbose_name='Identyfikator ryzyka', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='smshazardrev',
            name='company_area',
            field=models.CharField(verbose_name='Obszar firmy', choices=[('SALT', 'SALT'), ('ATO', 'ATO'), ('AOC', 'AOC'), ('SPO', 'SPO'), ('Inne', 'Inne')], max_length=10),
        ),
    ]
