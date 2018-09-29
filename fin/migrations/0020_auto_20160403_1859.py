# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fin', '0019_contractor_debet_allowed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balanceoperation',
            name='type',
            field=models.CharField(verbose_name='Rodzaj operacji', choices=[('Wpłata', 'Wpłata'), ('Wypłata', 'Wypłata'), ('Korekta', 'Korekta'), ('Usługa AOC', 'Usługa AOC'), ('Usługa SPO', 'Usługa SPO'), ('Wynajem', 'Wynajem'), ('Szkolenie', 'Szkolenie'), ('Egzamin', 'Egzamin'), ('Instruktor', 'Instruktor'), ('Zakup pakietu', 'Zakup pakietu'), ('Zwrot za pakiet', 'Zwrot za pakiet'), ('Zwrot za paliwo', 'Zwrot za paliwo')], max_length=15),
        ),
    ]
