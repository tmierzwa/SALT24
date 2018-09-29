# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ato', '0025_auto_20160114_1828'),
        ('fin', '0011_auto_20160114_1141'),
        ('panel', '0008_pilot_employee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pdt',
            old_name='instr',
            new_name='instructor',
        ),
        migrations.RemoveField(
            model_name='operation',
            name='operation_type',
        ),
        migrations.RemoveField(
            model_name='pdt',
            name='fuel_post',
        ),
        migrations.RemoveField(
            model_name='pdt',
            name='n1_cycles',
        ),
        migrations.RemoveField(
            model_name='pdt',
            name='n2_cycles',
        ),
        migrations.AddField(
            model_name='pdt',
            name='check_user',
            field=models.ForeignKey(related_name='pdt_checked_by_set', null=True, verbose_name='Sprawdzony przez', to='panel.FBOUser', blank=True),
        ),
        migrations.AddField(
            model_name='pdt',
            name='chect_time',
            field=models.DateTimeField(null=True, verbose_name='Czas sprawdzenia', blank=True),
        ),
        migrations.AddField(
            model_name='pdt',
            name='close_user',
            field=models.ForeignKey(related_name='pdt_closed_by_set', null=True, verbose_name='Zamknięty przez', to='panel.FBOUser', blank=True),
        ),
        migrations.AddField(
            model_name='pdt',
            name='contractor',
            field=models.ForeignKey(to='fin.Contractor', null=True, verbose_name='Kontrahent', blank=True),
        ),
        migrations.AddField(
            model_name='pdt',
            name='ext_voucher',
            field=models.CharField(null=True, verbose_name='Voucher obcy', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='pdt',
            name='flight_type',
            field=models.CharField(verbose_name='Rodzaj lotu', max_length=3, default='04'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pdt',
            name='open_user',
            field=models.ForeignKey(related_name='pdt_open_by_set', verbose_name='Otwiarty przez', default=1, to='panel.FBOUser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pdt',
            name='service_remarks',
            field=models.TextField(null=True, verbose_name='Opis usługi', blank=True),
        ),
        migrations.AddField(
            model_name='pdt',
            name='training',
            field=models.ForeignKey(to='ato.Training_inst', null=True, verbose_name='Szkolenie', blank=True),
        ),
        migrations.AddField(
            model_name='pdt',
            name='voucher',
            field=models.ForeignKey(to='fin.Voucher', null=True, verbose_name='Voucher', blank=True),
        ),
        migrations.AlterField(
            model_name='pdt',
            name='aircraft',
            field=models.ForeignKey(to='camo.Aircraft', verbose_name='Statek powietrzny'),
        ),
        migrations.AlterField(
            model_name='pdt',
            name='pic',
            field=models.ForeignKey(related_name='pdt_pic_set', verbose_name='Pierwszy pilot', to='panel.Pilot'),
        ),
        migrations.AlterField(
            model_name='pdt',
            name='remarks',
            field=models.TextField(null=True, verbose_name='Uwagi', blank=True),
        ),
    ]
