# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0006_auto_20150821_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smsevent',
            name='aircraft',
            field=models.CharField(verbose_name='Statek powietrzny', max_length=10),
        ),
        migrations.AlterField(
            model_name='smsevent',
            name='event_type',
            field=models.CharField(choices=[('Zdarzenie', 'Zdarzenie'), ('Incydent', 'Incydent'), ('Poważny Incydent', 'Powazny Incydent'), ('Wypadek', 'Wypadek')], verbose_name='Kwalifikacja zdarzenia', max_length=20),
        ),
        migrations.AlterField(
            model_name='smsevent',
            name='pic',
            field=models.CharField(verbose_name='Pilot dowódca', max_length=40),
        ),
    ]
