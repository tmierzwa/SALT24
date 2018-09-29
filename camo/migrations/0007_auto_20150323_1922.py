# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0006_auto_20150322_1556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aircraft',
            name='arc_date',
        ),
        migrations.RemoveField(
            model_name='aircraft',
            name='wb_date',
        ),
        migrations.AddField(
            model_name='aircraft',
            name='hours_count',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aircraft',
            name='landings_count',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aircraft',
            name='months_count',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
