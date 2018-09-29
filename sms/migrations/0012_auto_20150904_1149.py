# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0011_auto_20150824_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smsfailure',
            name='failure_date',
            field=models.DateField(verbose_name='Data zgłoszenia'),
        ),
    ]
