# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0038_pot_group_done_aso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operation',
            name='hours',
        ),
        migrations.AddField(
            model_name='operation',
            name='tth_end',
            field=models.DecimalField(max_digits=6, default=0, verbose_name='Licznik końcowy', decimal_places=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='operation',
            name='tth_start',
            field=models.DecimalField(max_digits=6, default=0, verbose_name='Licznik początkowy', decimal_places=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='operation',
            name='landings',
            field=models.IntegerField(verbose_name='Liczba lądowań'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='operation',
            name='operation_date',
            field=models.DateField(verbose_name='Data operacji'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='operation',
            name='pdt_ref',
            field=models.CharField(max_length=30, verbose_name='PDT Ref.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pot_group',
            name='done_aso',
            field=models.ForeignKey(verbose_name='Organizacja', to='camo.ASO'),
            preserve_default=True,
        ),
    ]
