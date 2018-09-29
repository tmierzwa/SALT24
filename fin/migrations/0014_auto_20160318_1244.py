# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0025_pdt_ms_report'),
        ('fin', '0013_auto_20160308_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='balanceoperation',
            name='pdt',
            field=models.ForeignKey(to='panel.PDT', verbose_name='Powiązany PDT', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='balanceoperation',
            name='type',
            field=models.CharField(choices=[('Wpłata', 'Wpłata'), ('Wypłata', 'Wypłata'), ('Korekta', 'Korekta'), ('Usługa AOC', 'Usługa AOC'), ('Usługa SPO', 'Usługa SPO'), ('Wynajem', 'Wynajem'), ('Szkolenie', 'Szkolenie'), ('Instruktor', 'Instruktor'), ('Zwrot za paliwo', 'Zwrot za paliwo')], verbose_name='Rodzaj operacji', max_length=10),
        ),
    ]
