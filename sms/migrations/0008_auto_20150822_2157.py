# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0007_auto_20150822_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smsevent',
            name='closure',
            field=models.CharField(verbose_name='Zamknięcie badania / raport końcowy', max_length=30),
        ),
        migrations.AlterField(
            model_name='smsevent',
            name='event_type',
            field=models.CharField(verbose_name='Kwalifikacja zdarzenia', max_length=20, choices=[('Zdarzenie', 'Zdarzenie'), ('Incydent', 'Incydent'), ('Poważny incydent', 'Powazny Incydent'), ('Wypadek', 'Wypadek')]),
        ),
        migrations.AlterField(
            model_name='smsevent',
            name='oper_type',
            field=models.CharField(verbose_name='Rodzaj operacji', max_length=10, choices=[('AOC', 'AOC'), ('ATO', 'ATO'), ('Wynajem', 'Wynajem'), ('Prywatny', 'Prywatny'), ('Inne', 'Inne')]),
        ),
    ]
