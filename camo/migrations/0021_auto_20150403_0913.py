# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0020_crs_crs_line'),
    ]

    operations = [
        migrations.AddField(
            model_name='pot_event',
            name='done_crs',
            field=models.ForeignKey(blank=True, to='camo.CRS', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pot_event',
            name='done_date',
            field=models.DateField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pot_event',
            name='done_hours',
            field=models.DecimalField(decimal_places=1, blank=True, max_digits=6, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pot_event',
            name='done_landings',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pot_event',
            name='done_months',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pot_group',
            name='POT_ref',
            field=models.CharField(max_length=100, default='POT-ref'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pot_group',
            name='done_crs',
            field=models.ForeignKey(blank=True, to='camo.CRS', null=True),
            preserve_default=True,
        ),
    ]
