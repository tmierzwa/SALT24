# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ato', '0032_auto_20160316_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Data wprowadenia programu'),
        ),
    ]
