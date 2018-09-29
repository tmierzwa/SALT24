# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-12 11:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0047_auto_20170115_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdt',
            name='failure_desc',
            field=models.TextField(blank=True, null=True, verbose_name='Opis usterki'),
        ),
        migrations.AddField(
            model_name='pdt',
            name='reapair_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pdt_repaired_by_set', to='panel.FBOUser', verbose_name='Usunięta przez'),
        ),
        migrations.AddField(
            model_name='pdt',
            name='repair_desc',
            field=models.TextField(blank=True, null=True, verbose_name='Sposób usunięcia'),
        ),
        migrations.AddField(
            model_name='pdt',
            name='repair_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Czas usunięcia'),
        ),
    ]
