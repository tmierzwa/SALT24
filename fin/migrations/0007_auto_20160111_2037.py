# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fin', '0006_contractor_remarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractor',
            name='address1',
            field=models.CharField(null=True, blank=True, max_length=100, verbose_name='Adres kontrahenta'),
        ),
        migrations.AlterField(
            model_name='contractor',
            name='address2',
            field=models.CharField(null=True, blank=True, max_length=100, verbose_name='Adres kontrahenta'),
        ),
    ]
