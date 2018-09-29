# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0042_auto_20150411_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pot_event',
            name='POT_ref',
            field=models.CharField(verbose_name='POT Ref.', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pot_event',
            name='done_crs',
            field=models.CharField(blank=True, verbose_name='Wykonano (CRS Ref.)', null=True, max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pot_event',
            name='done_date',
            field=models.DateField(blank=True, verbose_name='Wykonano (data)', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pot_event',
            name='done_hours',
            field=models.DecimalField(decimal_places=1, blank=True, verbose_name='Wykonano (TTH)', null=True, max_digits=6),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pot_event',
            name='done_landings',
            field=models.IntegerField(blank=True, verbose_name='Wykonano (lądowania)', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pot_group',
            name='done_aso',
            field=models.ForeignKey(blank=True, verbose_name='Wykonano (ASO)', to='camo.ASO', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pot_group',
            name='done_crs',
            field=models.CharField(blank=True, verbose_name='Wykonano (CRS Ref.)', null=True, max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pot_group',
            name='done_date',
            field=models.DateField(blank=True, verbose_name='Wykonano (data)', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pot_group',
            name='done_hours',
            field=models.DecimalField(decimal_places=1, blank=True, verbose_name='Wykonano (TTH)', null=True, max_digits=6),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pot_group',
            name='done_landings',
            field=models.IntegerField(blank=True, verbose_name='Wykonano (lądowania)', null=True),
            preserve_default=True,
        ),
    ]
