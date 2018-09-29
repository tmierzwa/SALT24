# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0003_auto_20150712_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdt',
            name='date',
            field=models.DateField(verbose_name='Data PDT', default=datetime.datetime(2015, 7, 12, 17, 16, 26, 574111, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pdt',
            name='remarks',
            field=models.CharField(max_length=350, verbose_name='Uwagi', default=''),
            preserve_default=False,
        ),
    ]
