# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0068_auto_20151017_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraft',
            name='hours_count',
            field=models.DecimalField(decimal_places=2, verbose_name='Licznik TTH', max_digits=7, default=0),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='from_hours',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='to_hours',
            field=models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='camo_operation',
            name='tth_end',
            field=models.DecimalField(decimal_places=2, verbose_name='Licznik końcowy', max_digits=7),
        ),
        migrations.AlterField(
            model_name='camo_operation',
            name='tth_start',
            field=models.DecimalField(decimal_places=2, verbose_name='Licznik początkowy', max_digits=7),
        ),
        migrations.AlterField(
            model_name='modification',
            name='done_hours',
            field=models.DecimalField(decimal_places=2, verbose_name='TTH wykonania', max_digits=7),
        ),
        migrations.AlterField(
            model_name='part',
            name='hours_count',
            field=models.DecimalField(decimal_places=2, verbose_name='Licznik TTH', max_digits=7, default=0),
        ),
        migrations.AlterField(
            model_name='pot_event',
            name='done_hours',
            field=models.DecimalField(null=True, verbose_name='Wykonano (TTH)', decimal_places=2, max_digits=7, blank=True),
        ),
        migrations.AlterField(
            model_name='pot_group',
            name='done_hours',
            field=models.DecimalField(null=True, verbose_name='Wykonano (TTH)', decimal_places=2, max_digits=7, blank=True),
        ),
        migrations.AlterField(
            model_name='pot_group',
            name='due_hours',
            field=models.DecimalField(null=True, verbose_name='Limit TTH', decimal_places=2, max_digits=7, blank=True),
        ),
        migrations.AlterField(
            model_name='wb_report',
            name='done_hours',
            field=models.DecimalField(decimal_places=2, verbose_name='TTH wykonania', max_digits=7),
        ),
        migrations.AlterField(
            model_name='wb_report',
            name='lat_cg',
            field=models.DecimalField(null=True, verbose_name='Lateral C.G.', decimal_places=3, max_digits=7, blank=True),
        ),
        migrations.AlterField(
            model_name='wb_report',
            name='lat_moment',
            field=models.DecimalField(null=True, verbose_name='Lateral moment', decimal_places=3, max_digits=7, blank=True),
        ),
        migrations.AlterField(
            model_name='wb_report',
            name='lon_cg',
            field=models.DecimalField(null=True, verbose_name='Longitudal C.G.', decimal_places=3, max_digits=7, blank=True),
        ),
        migrations.AlterField(
            model_name='wb_report',
            name='lon_moment',
            field=models.DecimalField(null=True, verbose_name='Longitudal moment', decimal_places=3, max_digits=7, blank=True),
        ),
        migrations.AlterField(
            model_name='work_order_line',
            name='done_hours',
            field=models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=7),
        ),
    ]
