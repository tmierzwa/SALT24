# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0093_camo_operation_pdt_ref'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraft',
            name='status',
            field=models.CharField(max_length=10, verbose_name='Status użytkowania', choices=[('flying', 'W użytkowaniu'), ('damaged', 'Uszkodzony'), ('parked', 'Zaparkowany')]),
        ),
    ]
