# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0031_auto_20150406_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wb_report',
            name='doc_ref',
            field=models.CharField(verbose_name='Numer dokumentu', blank=True, max_length=20, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='wb_report',
            name='done_doc',
            field=models.CharField(verbose_name='Numer dokumentu', blank=True, max_length=20, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='wb_report',
            name='lat_cg',
            field=models.DecimalField(verbose_name='Lateral C.G.', blank=True, decimal_places=2, max_digits=6, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='wb_report',
            name='lat_moment',
            field=models.DecimalField(verbose_name='Lateral moment', blank=True, decimal_places=2, max_digits=6, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='wb_report',
            name='lon_cg',
            field=models.DecimalField(verbose_name='Longitudal C.G.', blank=True, decimal_places=2, max_digits=6, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='wb_report',
            name='lon_moment',
            field=models.DecimalField(verbose_name='Longitudal moment', blank=True, decimal_places=2, max_digits=6, null=True),
            preserve_default=True,
        ),
    ]
