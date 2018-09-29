# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0012_pdt_fuel_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='pilot',
            name='email',
            field=models.EmailField(blank=True, verbose_name='Adres email', null=True, max_length=75),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pilot',
            name='pracownik',
            field=models.BooleanField(verbose_name='Pracownik SALT', default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pilot',
            name='telefon',
            field=models.CharField(blank=True, verbose_name='Telefon kontaktowy', null=True, max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pilot',
            name='upowaznienie',
            field=models.CharField(blank=True, verbose_name='Upowa?nienie SALT', null=True, max_length=100),
            preserve_default=True,
        ),
    ]
