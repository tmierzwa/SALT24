# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0036_auto_20150408_2259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crs',
            name='work_order',
        ),
        migrations.RemoveField(
            model_name='crs_line',
            name='crs',
        ),
        migrations.RemoveField(
            model_name='crs_line',
            name='pot_event',
        ),
        migrations.DeleteModel(
            name='CRS_line',
        ),
        migrations.RemoveField(
            model_name='work_order',
            name='done_date',
        ),
        migrations.RemoveField(
            model_name='work_order',
            name='done_hours',
        ),
        migrations.AddField(
            model_name='work_order_line',
            name='done_crs',
            field=models.CharField(null=True, blank=True, max_length=20),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='work_order_line',
            name='done_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='work_order_line',
            name='done_hours',
            field=models.DecimalField(null=True, blank=True, decimal_places=1, max_digits=6),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pot_event',
            name='POT_ref',
            field=models.CharField(max_length=100, verbose_name='PO Ref.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pot_event',
            name='done_crs',
            field=models.CharField(null=True, blank=True, verbose_name='Numer CRS', max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pot_event',
            name='done_date',
            field=models.DateField(null=True, blank=True, verbose_name='Data wykonania'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pot_event',
            name='done_hours',
            field=models.DecimalField(null=True, blank=True, decimal_places=1, verbose_name='TTH wykonania', max_digits=6),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pot_event',
            name='name',
            field=models.CharField(max_length=800, verbose_name='Nazwa czynności'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pot_group',
            name='done_crs',
            field=models.CharField(null=True, blank=True, verbose_name='Dokument CRS', max_length=20),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='CRS',
        ),
        migrations.AlterField(
            model_name='work_order',
            name='date',
            field=models.DateField(default=datetime.date(2015, 4, 9)),
            preserve_default=True,
        ),
    ]
