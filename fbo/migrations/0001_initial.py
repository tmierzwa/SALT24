# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-24 15:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info_priority', models.TextField(blank=True, null=True, verbose_name='Ważne informacje na stronie startowej')),
                ('info_body', models.TextField(blank=True, null=True, verbose_name='Pozstałe informacje na stronie startowej')),
                ('info_contact', models.TextField(blank=True, null=True, verbose_name='Informacje kontaktowe na stronie startowej')),
            ],
        ),
    ]
