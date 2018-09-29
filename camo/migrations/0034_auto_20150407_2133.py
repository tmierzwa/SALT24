# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0033_auto_20150406_1242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pot_event',
            name='done_months',
        ),
        migrations.RemoveField(
            model_name='pot_group',
            name='done_months',
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='insurance_date',
            field=models.DateField(blank=True, verbose_name='Ważność ubezp', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ata',
            name='chapter',
            field=models.CharField(verbose_name='Rozdział', max_length=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ata',
            name='chapter_title',
            field=models.CharField(verbose_name='Tytuł rozdziału', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ata',
            name='description',
            field=models.CharField(verbose_name='Opis', max_length=1000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ata',
            name='section',
            field=models.CharField(verbose_name='Sekcja', max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ata',
            name='section_title',
            field=models.CharField(verbose_name='Tytuł sekcji', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='crs',
            name='done_date',
            field=models.DateField(default=datetime.date(2015, 4, 7)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pot_group',
            name='done_crs',
            field=models.ForeignKey(verbose_name='Dokument CRS', blank=True, to='camo.CRS', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pot_group',
            name='done_date',
            field=models.DateField(blank=True, verbose_name='Data wykonania', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pot_group',
            name='done_hours',
            field=models.DecimalField(max_digits=6, blank=True, verbose_name='TTH wykonania', null=True, decimal_places=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='work_order',
            name='date',
            field=models.DateField(default=datetime.date(2015, 4, 7)),
            preserve_default=True,
        ),
    ]
