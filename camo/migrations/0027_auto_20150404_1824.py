# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0026_auto_20150404_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pot_group',
            name='months_count',
        ),
        migrations.AddField(
            model_name='pot_group',
            name='count_type',
            field=models.CharField(choices=[('production', 'Od produkcji/remontu'), ('install', 'Od instalacji')], default='production', max_length=10, verbose_name='Sposób liczenia'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pot_group',
            name='cyclic',
            field=models.BooleanField(default=True, verbose_name='Czynność cykliczna'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pot_group',
            name='optional',
            field=models.BooleanField(default=False, verbose_name='Czynność opcjonalna'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pot_group',
            name='parked',
            field=models.BooleanField(default=False, verbose_name='Czynność postojowa'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pot_group',
            name='type',
            field=models.CharField(choices=[('oth', 'Obsługa techniczna'), ('llp', 'Planowy demontaż'), ('ovh', 'Planowy remont')], default='oth', max_length=10, verbose_name='Rodzaj czynności'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='part',
            name='lifecycle',
            field=models.CharField(choices=[('llp', 'Ograniczona żywotność (LLP)'), ('ovh', 'Podlegająca remontowi (OVH)'), ('oth', 'Według stanu')], default='oth', max_length=10, verbose_name='Cykl życia'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pot_group',
            name='POT_ref',
            field=models.CharField(max_length=100, verbose_name='POT ref.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pot_group',
            name='due_hours',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=6, null=True, verbose_name='Limit TTH'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pot_group',
            name='due_landings',
            field=models.IntegerField(blank=True, null=True, verbose_name='Limit lądowań'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pot_group',
            name='due_months',
            field=models.IntegerField(blank=True, null=True, verbose_name='Limit miesięcy'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pot_group',
            name='hours_count',
            field=models.DecimalField(default=0, max_digits=6, decimal_places=1, verbose_name='Licznik TTH'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pot_group',
            name='landings_count',
            field=models.IntegerField(default=0, verbose_name='Licznik lądowań'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pot_group',
            name='name',
            field=models.CharField(max_length=500, verbose_name='Opis'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pot_group',
            name='part',
            field=models.ForeignKey(to='camo.Part', verbose_name='Powiązana część'),
            preserve_default=True,
        ),
    ]
