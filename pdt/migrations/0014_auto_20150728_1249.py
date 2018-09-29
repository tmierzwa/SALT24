# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0013_auto_20150728_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Duty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date', models.DateField(verbose_name='Data')),
                ('company', models.CharField(max_length=10, default='salt', verbose_name='Firma', choices=[('salt', 'SALT'), ('other', 'Poza SALT')])),
                ('role', models.CharField(max_length=50, null=True, verbose_name='Stnowisko', blank=True)),
                ('duty_type', models.CharField(max_length=50, null=True, verbose_name='Rodzaj obowiązków', blank=True)),
                ('duty_time', models.DecimalField(decimal_places=1, verbose_name='Czas pracy', max_digits=4)),
                ('block_time', models.DecimalField(null=True, blank=True, verbose_name='Czas służby', decimal_places=1, max_digits=4)),
                ('pracownik', models.BooleanField(default=False, verbose_name='Pracownik SALT')),
                ('remarks', models.CharField(max_length=350, null=True, verbose_name='Uwagi', blank=True)),
                ('pilot', models.ForeignKey(to='pdt.Pilot')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='operation',
            name='bags',
            field=models.IntegerField(null=True, blank=True, verbose_name='Ciężar bagazu [kg]'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='operation',
            name='fuel_refill',
            field=models.IntegerField(default=0, verbose_name='Uzupełnione paliwo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='operation',
            name='fuel_used',
            field=models.IntegerField(verbose_name='Paliwo zużyte'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='operation',
            name='hydr_oil_refill',
            field=models.DecimalField(null=True, decimal_places=1, verbose_name='Uzupełniony olej hydr.', max_digits=3, default=0, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='operation',
            name='landings',
            field=models.IntegerField(verbose_name='Liczba lądowań'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='operation',
            name='loc_end',
            field=models.CharField(max_length=20, verbose_name='Miejsce lądowania'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='operation',
            name='oil_lh_refill',
            field=models.DecimalField(default=0, decimal_places=1, verbose_name='Uzupełniony olej', max_digits=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='operation',
            name='oil_rh_refill',
            field=models.DecimalField(default=0, decimal_places=1, verbose_name='Uzupełniony olej RH', max_digits=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='operation',
            name='pax',
            field=models.IntegerField(null=True, blank=True, verbose_name='Liczba pasażerow'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='operation',
            name='trans_oil_refill',
            field=models.DecimalField(null=True, decimal_places=1, verbose_name='Uzupełniony olej przekł.', max_digits=3, default=0, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='operation',
            name='trans_oil_state',
            field=models.CharField(max_length=3, null=True, verbose_name='Olej przekł. w normie', choices=[('ok', 'OK')], blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='operation',
            name='tth_end',
            field=models.DecimalField(decimal_places=1, verbose_name='Licznik końcowy', max_digits=6),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='operation',
            name='tth_start',
            field=models.DecimalField(decimal_places=1, verbose_name='Licznik początkowy', max_digits=6),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pdt',
            name='close_time',
            field=models.DateTimeField(null=True, blank=True, verbose_name='Czas zamknięcia'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pdt',
            name='fuel_post',
            field=models.IntegerField(null=True, default=0, verbose_name='Uzupełnione paliwo', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pdt',
            name='instr',
            field=models.ForeignKey(null=True, verbose_name='Instruktor nadzorujący', related_name='pdt_instr_set', blank=True, to='pdt.Pilot'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pdt',
            name='status',
            field=models.CharField(max_length=10, default='open', verbose_name='Status', choices=[('open', 'Otwarty'), ('closed', 'Zamknięty'), ('checked', 'Sprawdzony')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pilot',
            name='imie',
            field=models.CharField(max_length=100, verbose_name='Imię'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pilot',
            name='upowaznienie',
            field=models.CharField(max_length=100, null=True, verbose_name='Upoważnienie SALT', blank=True),
            preserve_default=True,
        ),
    ]
