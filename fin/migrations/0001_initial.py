# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0083_auto_20160106_1716'),
        ('pdt', '0021_auto_20151216_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuelBurn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fuel_volume', models.DecimalField(verbose_name='Objętość paliwa (L)', max_digits=4, decimal_places=1)),
                ('pdt_operation', models.ForeignKey(verbose_name='Operacja PDT', to='pdt.Operation')),
            ],
        ),
        migrations.CreateModel(
            name='FuelCorrection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Data protokołu różnic')),
                ('document', models.CharField(max_length=30, verbose_name='Dokument protokołu różnic', null=True, blank=True)),
                ('fuel_volume', models.DecimalField(verbose_name='Objętość różnicy (L)', max_digits=6, decimal_places=1)),
                ('remarks', models.TextField(verbose_name='Uwagi', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='FuelDelivery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('provider', models.CharField(max_length=50, verbose_name='Dostawca paliwa', null=True, blank=True)),
                ('date', models.DateField(verbose_name='Data dostawy')),
                ('document', models.CharField(max_length=30, verbose_name='Dokument dostawy', null=True, blank=True)),
                ('fuel_volume', models.DecimalField(verbose_name='Objętość paliwa (L)', max_digits=6, decimal_places=1)),
                ('liter_price', models.DecimalField(verbose_name='Cena za litr (PLN)', max_digits=5, decimal_places=2)),
                ('remarks', models.TextField(verbose_name='Uwagi', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='FuelTank',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Zbiornik paliwa')),
                ('fuel_type', models.CharField(max_length=5, verbose_name='Rodzaj paliwa', choices=[('AVGAS', 'Avgas 100LL'), ('MOGAS', 'Benzyna samochodowa'), ('JETA1', 'Paliwo JET A-1')])),
                ('fuel_volume', models.DecimalField(verbose_name='Objętość paliwa (L)', max_digits=6, default=0, decimal_places=1)),
                ('remarks', models.TextField(verbose_name='Uwagi', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='FuelTransfer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Data wydania wew.')),
                ('document', models.CharField(max_length=30, verbose_name='Dokument wydania wew.', null=True, blank=True)),
                ('fuel_volume', models.DecimalField(verbose_name='Objętość paliwa (L)', max_digits=6, decimal_places=1)),
                ('liter_price', models.DecimalField(verbose_name='Średnia cena za litr (PLN)', max_digits=5, decimal_places=2)),
                ('remarks', models.TextField(verbose_name='Uwagi', null=True, blank=True)),
                ('fueltank_from', models.ForeignKey(to='fin.FuelTank', verbose_name='Zbiornik żródłowy', related_name='tank_from')),
                ('fueltank_to', models.ForeignKey(to='fin.FuelTank', verbose_name='Zbiornik docelowy', related_name='tank_to')),
            ],
        ),
        migrations.CreateModel(
            name='LocalFueling',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Data tankowania')),
                ('person', models.CharField(max_length=50, verbose_name='Osoba tankująca', null=True, blank=True)),
                ('fuel_volume', models.DecimalField(verbose_name='Objętość paliwa (L)', max_digits=4, decimal_places=1)),
                ('remarks', models.TextField(verbose_name='Uwagi', null=True, blank=True)),
                ('aircraft', models.ForeignKey(verbose_name='Statek powietrzny', to='camo.Aircraft')),
                ('fueltank', models.ForeignKey(verbose_name='Zbiornik paliwa', to='fin.FuelTank')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('module', models.BooleanField()),
            ],
            options={
                'permissions': (('access_module', 'Dostęp do modułu FIN'),),
            },
        ),
        migrations.CreateModel(
            name='PDTFueling',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fuel_volume', models.DecimalField(verbose_name='Objętość paliwa (L)', max_digits=4, decimal_places=1)),
                ('fueltank', models.ForeignKey(verbose_name='Zbiornik paliwa', to='fin.FuelTank')),
                ('pdt', models.ForeignKey(verbose_name='PDT', to='pdt.PDT')),
            ],
        ),
        migrations.CreateModel(
            name='RemoteFueling',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(max_length=30, verbose_name='Lotnisko tankowania', null=True, blank=True)),
                ('fuel_volume', models.DecimalField(verbose_name='Objętość paliwa (L)', max_digits=4, decimal_places=1)),
                ('document', models.CharField(max_length=30, verbose_name='Faktura za tankowanie', null=True, blank=True)),
                ('excise', models.CharField(max_length=30, verbose_name='Dowód dostawy', null=True, blank=True)),
                ('total_price', models.DecimalField(verbose_name='Wartość paliwa (PLN)', max_digits=7, decimal_places=2)),
                ('remarks', models.TextField(verbose_name='Uwagi', null=True, blank=True)),
                ('pdt', models.ForeignKey(verbose_name='PDT', to='pdt.PDT')),
            ],
        ),
        migrations.AddField(
            model_name='fueldelivery',
            name='fueltank',
            field=models.ForeignKey(verbose_name='Zbiornik paliwa', to='fin.FuelTank'),
        ),
        migrations.AddField(
            model_name='fuelcorrection',
            name='fueltank',
            field=models.ForeignKey(verbose_name='Zbiornik paliwa', to='fin.FuelTank'),
        ),
    ]
