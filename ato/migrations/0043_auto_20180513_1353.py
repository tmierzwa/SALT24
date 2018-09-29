# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-13 11:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ato', '0042_auto_20180512_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='card_entry',
            name='instructor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='ato.Instructor', verbose_name=b'Instructor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card_entry',
            name='training_inst',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='ato.Training_inst', verbose_name=b'Szkolenie'),
            preserve_default=False,
        ),
    ]