# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0017_auto_20150804_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pilot',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Adres email', null=True, blank=True),
        ),
    ]
