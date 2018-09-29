# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ato', '0019_auto_20151103_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise_flight',
            name='operation',
            field=models.ForeignKey(verbose_name='Operacja z PDT', to='panel.Operation'),
        ),
    ]
