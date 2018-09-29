# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0008_auto_20150822_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smsevent',
            name='closure',
            field=models.CharField(max_length=30, null=True, blank=True, verbose_name='Zamknięcie badania / raport końcowy'),
        ),
    ]
