# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-13 10:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0051_auto_20170525_2032'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='operation',
            options={'ordering': ['operation_no']},
        ),
    ]