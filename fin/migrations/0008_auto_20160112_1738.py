# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fin', '0007_auto_20160111_2037'),
    ]

    operations = [
        migrations.CreateModel(
            name='BalanceOperation',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Data operacji')),
                ('type', models.CharField(max_length=10, choices=[('Wpłata', 'Wpłata'), ('Wypłata', 'Wypłata'), ('Korekta', 'Korekta')], verbose_name='Rodzaj operacji')),
                ('document', models.CharField(blank=True, max_length=30, null=True, verbose_name='Dokument operacji')),
                ('ato_amount', models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Kwota operacji (szkolenia)')),
                ('rent_amount', models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Kwota operacji (wynajem)')),
                ('aoc_amount', models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Kwota operacji (AOC)')),
                ('spo_amount', models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Kwota operacji (SPO)')),
                ('remarks', models.TextField(blank=True, null=True, verbose_name='Uwagi')),
            ],
        ),
        migrations.AlterField(
            model_name='contractor',
            name='aoc_balance',
            field=models.DecimalField(decimal_places=2, max_digits=8, default=0, verbose_name='Saldo AOC'),
        ),
        migrations.AlterField(
            model_name='contractor',
            name='ato_balance',
            field=models.DecimalField(decimal_places=2, max_digits=8, default=0, verbose_name='Saldo szkoleń'),
        ),
        migrations.AlterField(
            model_name='contractor',
            name='rent_balance',
            field=models.DecimalField(decimal_places=2, max_digits=8, default=0, verbose_name='Saldo wynajmu'),
        ),
        migrations.AlterField(
            model_name='contractor',
            name='spo_balance',
            field=models.DecimalField(decimal_places=2, max_digits=8, default=0, verbose_name='Saldo usług'),
        ),
        migrations.AddField(
            model_name='balanceoperation',
            name='contractor',
            field=models.ForeignKey(to='fin.Contractor', verbose_name='Kontrahent'),
        ),
    ]
