# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0013_auto_20150331_1152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='part',
            name='hours_adjustment',
        ),
        migrations.RemoveField(
            model_name='part',
            name='hours_start',
        ),
        migrations.RemoveField(
            model_name='part',
            name='landings_adjustment',
        ),
        migrations.RemoveField(
            model_name='part',
            name='landings_start',
        ),
        migrations.RemoveField(
            model_name='part',
            name='months_adjustment',
        ),
        migrations.RemoveField(
            model_name='part',
            name='months_start',
        ),
        migrations.AddField(
            model_name='pot_group',
            name='hours_count',
            field=models.DecimalField(decimal_places=1, max_digits=6, default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pot_group',
            name='landings_count',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pot_group',
            name='months_count',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='hours_count',
            field=models.DecimalField(decimal_places=1, max_digits=6, default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='assignment',
            name='from_hours',
            field=models.DecimalField(decimal_places=1, max_digits=6, default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='assignment',
            name='to_hours',
            field=models.DecimalField(blank=True, null=True, decimal_places=1, max_digits=6),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='operation',
            name='hours',
            field=models.DecimalField(decimal_places=1, max_digits=6),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='part',
            name='hours_count',
            field=models.DecimalField(decimal_places=1, max_digits=6, default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pot_group',
            name='done_hours',
            field=models.DecimalField(blank=True, null=True, decimal_places=1, max_digits=6),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pot_group',
            name='due_hours',
            field=models.DecimalField(blank=True, null=True, decimal_places=1, max_digits=6),
            preserve_default=True,
        ),
    ]
