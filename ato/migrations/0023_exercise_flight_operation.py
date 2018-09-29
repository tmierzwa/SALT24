# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0006_auto_20160114_1349'),
        ('ato', '0022_remove_exercise_flight_operation'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise_flight',
            name='operation',
            field=models.ForeignKey(verbose_name='Operacja z PDT', to='panel.Operation', default=1),
            preserve_default=False,
        ),
    ]
