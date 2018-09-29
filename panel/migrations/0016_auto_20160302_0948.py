# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0015_auto_20160302_0937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operation',
            name='Liczba cykli',
        ),
        migrations.AddField(
            model_name='operation',
            name='cycles',
            field=models.IntegerField(verbose_name='Liczba cykli', default=0),
        ),
    ]
