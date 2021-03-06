# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fin', '0016_auto_20160320_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balanceoperation',
            name='type',
            field=models.CharField(choices=[('Wpłata', 'Wpłata'), ('Wypłata', 'Wypłata'), ('Korekta', 'Korekta'), ('Usługa AOC', 'Usługa AOC'), ('Usługa SPO', 'Usługa SPO'), ('Wynajem', 'Wynajem'), ('Szkolenie', 'Szkolenie'), ('Egzamin', 'Egzamin'), ('Instruktor', 'Instruktor'), ('Zwrot za paliwo', 'Zwrot za paliwo')], verbose_name='Rodzaj operacji', max_length=15),
        ),
    ]
