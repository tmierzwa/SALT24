# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0002_auto_20150313_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='hours_limit',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='landings_limit',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='months_limit',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item_as_part',
            name='to_date',
            field=models.DateField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item_as_part',
            name='to_hours',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='part',
            name='super_part',
            field=models.ForeignKey(to='camo.Part', blank=True, null=True),
            preserve_default=True,
        ),
    ]
