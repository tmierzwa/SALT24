# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-04 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('res', '0008_reservationfbo_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcefbo',
            name='color',
            field=models.CharField(default='#cdcdcd', max_length=7, verbose_name='Kolor wyświetlania'),
        ),
        migrations.AlterField(
            model_name='resourcefbo',
            name='name',
            field=models.CharField(max_length=20, unique=True, verbose_name='Nazwa zasobu'),
        ),
    ]
