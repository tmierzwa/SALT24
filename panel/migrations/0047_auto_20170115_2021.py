# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-15 19:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0046_auto_20170103_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duty',
            name='pdt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='panel.PDT'),
        ),
        migrations.AlterField(
            model_name='fbouser',
            name='contractor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='fin.Contractor', verbose_name='Kontrahent'),
        ),
        migrations.AlterField(
            model_name='pdt',
            name='check_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pdt_checked_by_set', to='panel.FBOUser', verbose_name='Sprawdzony przez'),
        ),
        migrations.AlterField(
            model_name='pdt',
            name='close_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pdt_closed_by_set', to='panel.FBOUser', verbose_name='Zamknięty przez'),
        ),
        migrations.AlterField(
            model_name='pdt',
            name='contractor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='fin.Contractor', verbose_name='Kontrahent'),
        ),
        migrations.AlterField(
            model_name='pdt',
            name='instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pdt_instr_set', to='panel.Pilot', verbose_name='Instruktor nadzorujący'),
        ),
        migrations.AlterField(
            model_name='pdt',
            name='ms_report',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='camo.MS_report', verbose_name='Na podstawie MS'),
        ),
        migrations.AlterField(
            model_name='pdt',
            name='sic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pdt_sic_set', to='panel.Pilot', verbose_name='Drugi pilot'),
        ),
        migrations.AlterField(
            model_name='pdt',
            name='training',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ato.Training_inst', verbose_name='Szkolenie'),
        ),
        migrations.AlterField(
            model_name='pdt',
            name='voucher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='fin.Voucher', verbose_name='Voucher'),
        ),
    ]
