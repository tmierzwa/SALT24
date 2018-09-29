# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fin', '0009_auto_20160112_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='soldpackage',
            name='date',
            field=models.DateField(verbose_name='Data zakupu pakietu', default=datetime.datetime(2016, 1, 12, 19, 2, 3, 180408, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
