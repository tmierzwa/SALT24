# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0025_pdt_ms_report'),
        ('sms', '0018_auto_20160114_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='smsevent',
            name='reported_by',
            field=models.ForeignKey(blank=True, to='panel.FBOUser', null=True, verbose_name='Zgłaszający użytkownik'),
        ),
        migrations.AddField(
            model_name='smsreport',
            name='reported_by',
            field=models.ForeignKey(blank=True, to='panel.FBOUser', null=True, verbose_name='Zgłoszajacy użytkownik'),
        ),
        migrations.AlterField(
            model_name='smsevent',
            name='description',
            field=models.CharField(verbose_name='Opis zdarzenia', max_length=500),
        ),
        migrations.AlterField(
            model_name='smsreport',
            name='description',
            field=models.CharField(verbose_name='Treść zgłoszenia', max_length=500),
        ),
    ]
