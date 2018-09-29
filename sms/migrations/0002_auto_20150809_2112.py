# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='smsevent',
            old_name='pkwbl_date',
            new_name='pkbwl_date',
        ),
        migrations.AlterField(
            model_name='smsevent',
            name='aircraft',
            field=models.ForeignKey(to='camo.Aircraft', verbose_name='Statek powietrzny'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='smsevent',
            name='pic',
            field=models.ForeignKey(to='pdt.Pilot', verbose_name='Pilot dowódca'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='smshazard',
            name='hazard_date',
            field=models.DateField(verbose_name='Data wprowadzenia'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='smshazard',
            name='hazard_ref',
            field=models.CharField(max_length=10, verbose_name='Identyfikator zagrożenia'),
            preserve_default=True,
        ),
    ]
