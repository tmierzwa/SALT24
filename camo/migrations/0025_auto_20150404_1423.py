# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0024_aircraft_wb_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='lifecycle',
            field=models.CharField(default='oth', max_length=10, verbose_name='Cykl życia', choices=[('llp', 'Ograniczona żywotność (LLP)'), ('ovh', 'Podlegająca remontowi (OVH)'), ('oth', 'Według stanu')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='hours_count',
            field=models.DecimalField(max_digits=6, default=0, verbose_name='Licznik TTH', decimal_places=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='insurance_date',
            field=models.DateField(blank=True, verbose_name='Ważność ubezpieczenia', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='landings_count',
            field=models.IntegerField(default=0, verbose_name='Licznik lądowań'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='production_date',
            field=models.DateField(verbose_name='Data producji'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='registration',
            field=models.CharField(max_length=12, verbose_name='Rejestracja'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='status',
            field=models.CharField(max_length=10, choices=[('flying', 'W użytkowaniu'), ('parked', 'Zaparkowany')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='type',
            field=models.CharField(max_length=100, verbose_name='Typ SP'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='wb_date',
            field=models.DateField(blank=True, verbose_name='Ważność W&B', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='part',
            name='hours_count',
            field=models.DecimalField(max_digits=6, default=0, verbose_name='Licznik TTH', decimal_places=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='part',
            name='install_date',
            field=models.DateField(blank=True, verbose_name='Data instalacji', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='part',
            name='landings_count',
            field=models.IntegerField(default=0, verbose_name='Licznik lądowań'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='part',
            name='maker',
            field=models.CharField(max_length=100, verbose_name='Producent'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='part',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nazwa'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='part',
            name='production_date',
            field=models.DateField(verbose_name='Data produkcji'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='part',
            name='serial_no',
            field=models.CharField(max_length=30, verbose_name='Numer seryjny'),
            preserve_default=True,
        ),
    ]
