# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0011_operation_fuel_used'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdt',
            name='fuel_post',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Uzupe?nione paliwo'),
            preserve_default=True,
        ),
    ]
