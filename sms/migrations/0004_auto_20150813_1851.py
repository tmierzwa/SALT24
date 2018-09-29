# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0003_auto_20150811_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smshazard',
            name='hazard_type',
            field=models.CharField(max_length=10, choices=[('Zewnętrzne', 'Zewnętrzne'), ('Osobowe', 'Osobowe'), ('Operacyjne', 'Operacyjne'), ('Techniczne', 'Techniczne'), ('AS 350', 'AS 350'), ('Inne', 'Inne')], verbose_name='Klasa zagrożenia'),
        ),
        migrations.AlterField(
            model_name='smshazard',
            name='remarks',
            field=models.CharField(max_length=1000, verbose_name='Uwagi', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='smsrisk',
            name='description',
            field=models.CharField(max_length=1000, verbose_name='Szczegółowy opis natury ryzyka'),
        ),
        migrations.AlterField(
            model_name='smsrisk',
            name='mitigation',
            field=models.CharField(max_length=1000, verbose_name='Sposoby ograniczania ryzyka', null=True, blank=True),
        ),
    ]
