# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-08-06 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0053_fbouser_ncr_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fbouser',
            name='ncr_user',
            field=models.BooleanField(default=False, verbose_name='Odpowiedzialny w NCR'),
        ),
    ]