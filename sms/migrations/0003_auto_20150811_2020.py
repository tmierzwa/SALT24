# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0002_auto_20150809_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smsfailure',
            name='pdt_ref',
            field=models.ForeignKey(verbose_name='Numer PDT', to='pdt.PDT'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='smsrisk',
            name='init_impact',
            field=models.CharField(choices=[('E', 'E - Bardzo duża'), ('D', 'D - Duża'), ('C', 'C - Średnia'), ('B', 'B - Mała'), ('A', 'A - Bardzo mała')], max_length=1, verbose_name='Początkowa dotkliwość'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='smsrisk',
            name='init_probability',
            field=models.CharField(choices=[('5', '5 - Bardzo wysokie'), ('4', '4 - Wysokie'), ('3', '3 - Średnie'), ('2', '2 - Niskie'), ('1', '1 - Bardzo niskie')], max_length=1, verbose_name='Początkowe prawdopodobieństwo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='smsrisk',
            name='res_impact',
            field=models.CharField(choices=[('E', 'E - Bardzo duża'), ('D', 'D - Duża'), ('C', 'C - Średnia'), ('B', 'B - Mała'), ('A', 'A - Bardzo mała')], max_length=1, null=True, verbose_name='Szczątkowa dotkliwość', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='smsrisk',
            name='res_probability',
            field=models.CharField(choices=[('5', '5 - Bardzo wysokie'), ('4', '4 - Wysokie'), ('3', '3 - Średnie'), ('2', '2 - Niskie'), ('1', '1 - Bardzo niskie')], max_length=1, null=True, verbose_name='Szczątkowe prawdopodobieństwo', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='smsrisk',
            name='smshazard',
            field=models.ForeignKey(verbose_name='Zarejestrowane zagrożenie', to='sms.SMSHazard'),
            preserve_default=True,
        ),
    ]
