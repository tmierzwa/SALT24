# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fin', '0005_contractor_rentpackage'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractor',
            name='remarks',
            field=models.TextField(null=True, blank=True, verbose_name='Uwagi'),
        ),
    ]
