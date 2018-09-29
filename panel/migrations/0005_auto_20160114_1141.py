# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0085_auto_20160114_1141'),
        ('fin', '0011_auto_20160114_1141'),
        ('panel', '0004_auto_20151211_1308'),
    ]

    operations = [
        migrations.CreateModel(
            name='Duty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('date', models.DateField(verbose_name='Data')),
                ('company', models.CharField(verbose_name='Firma', max_length=10, default='salt', choices=[('salt', 'SALT'), ('other', 'Poza SALT')])),
                ('role', models.CharField(verbose_name='Stanowisko', blank=True, max_length=50, null=True)),
                ('duty_type', models.CharField(verbose_name='Rodzaj obowiązków', blank=True, max_length=50, null=True)),
                ('duty_time', models.DecimalField(verbose_name='Czas pracy', decimal_places=1, max_digits=4)),
                ('block_time', models.DecimalField(verbose_name='Czas służby', default=0, decimal_places=1, blank=True, max_digits=4, null=True)),
                ('remarks', models.CharField(verbose_name='Uwagi', blank=True, max_length=350, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('operation_no', models.IntegerField(verbose_name='Nr. rejsu', blank=True, null=True)),
                ('operation_type', models.CharField(verbose_name='Rodzaj lotu', max_length=3, choices=[('01', '01 - Przewóz lotniczy'), ('02', '02 - Usługi lotnicze'), ('03A', '03A - Szkolenie AOC'), ('03B', '03B - Szkolenie ATO'), ('04', '04 - Wynajem SP'), ('05', '05 - Loty niepłatne')])),
                ('pax', models.IntegerField(verbose_name='Liczba pasażerow', blank=True, null=True)),
                ('bags', models.IntegerField(verbose_name='Ciężar bagazu [kg]', blank=True, null=True)),
                ('fuel_refill', models.IntegerField(verbose_name='Uzupełnione paliwo', default=0)),
                ('fuel_available', models.IntegerField(verbose_name='Stan paliwa do lotu')),
                ('fuel_used', models.IntegerField(verbose_name='Paliwo zużyte')),
                ('oil_lh_refill', models.DecimalField(verbose_name='Uzupełniony olej', decimal_places=1, default=0, max_digits=3)),
                ('oil_rh_refill', models.DecimalField(verbose_name='Uzupełniony olej RH', decimal_places=1, default=0, max_digits=3)),
                ('oil_state', models.CharField(verbose_name='Olej w normie', blank=True, max_length=3, choices=[('ok', 'OK')], null=True)),
                ('trans_oil_refill', models.DecimalField(verbose_name='Uzupełniony olej przekł.', default=0, decimal_places=1, blank=True, max_digits=3, null=True)),
                ('trans_oil_state', models.CharField(verbose_name='Olej przekł. w normie', blank=True, max_length=3, choices=[('ok', 'OK')], null=True)),
                ('hydr_oil_refill', models.DecimalField(verbose_name='Uzupełniony olej hydr.', default=0, decimal_places=1, blank=True, max_digits=3, null=True)),
                ('hydr_oil_state', models.CharField(verbose_name='Olej hydr. w normie', blank=True, max_length=3, choices=[('ok', 'OK')], null=True)),
                ('loc_start', models.CharField(verbose_name='Miejsce startu', max_length=20)),
                ('time_start', models.TimeField(verbose_name='Czas off-block')),
                ('tth_start', models.DecimalField(verbose_name='Licznik początkowy', decimal_places=2, max_digits=7)),
                ('loc_end', models.CharField(verbose_name='Miejsce lądowania', max_length=20)),
                ('time_end', models.TimeField(verbose_name='Czas on-block')),
                ('tth_end', models.DecimalField(verbose_name='Licznik końcowy', decimal_places=2, max_digits=7)),
                ('landings', models.IntegerField(verbose_name='Liczba lądowań')),
            ],
        ),
        migrations.CreateModel(
            name='PDT',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('pdt_ref', models.IntegerField(verbose_name='Numer PDT')),
                ('date', models.DateField(verbose_name='Data PDT')),
                ('status', models.CharField(verbose_name='Status', max_length=10, default='open', choices=[('open', 'Otwarty'), ('closed', 'Zamknięty'), ('checked', 'Sprawdzony')])),
                ('n1_cycles', models.IntegerField(verbose_name='Liczba cykli N1', blank=True, null=True)),
                ('n2_cycles', models.IntegerField(verbose_name='Liczba cykli N2', blank=True, null=True)),
                ('fuel_post', models.IntegerField(verbose_name='Uzupełnione paliwo', blank=True, default=0, null=True)),
                ('remarks', models.CharField(verbose_name='Uwagi', blank=True, max_length=350, null=True)),
                ('open_time', models.DateTimeField(verbose_name='Czas otwarcia', auto_now_add=True)),
                ('close_time', models.DateTimeField(verbose_name='Czas zamknięcia', blank=True, null=True)),
                ('aircraft', models.ForeignKey(to='camo.Aircraft')),
            ],
        ),
        migrations.CreateModel(
            name='Pilot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('licence', models.CharField(verbose_name='Numer licencji', blank=True, max_length=50, null=True)),
                ('licence_date', models.DateField(verbose_name='Ważność licencji', blank=True, null=True)),
                ('medical', models.CharField(verbose_name='Badania lotnicze', blank=True, max_length=50, null=True)),
                ('medical_date', models.DateField(verbose_name='Ważność badań', blank=True, null=True)),
                ('clereance', models.CharField(verbose_name='Upoważnienie SALT', blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='fbouser',
            name='clereance',
        ),
        migrations.RemoveField(
            model_name='fbouser',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='fbouser',
            name='instructor',
        ),
        migrations.RemoveField(
            model_name='fbouser',
            name='licence',
        ),
        migrations.RemoveField(
            model_name='fbouser',
            name='licence_date',
        ),
        migrations.RemoveField(
            model_name='fbouser',
            name='medical',
        ),
        migrations.RemoveField(
            model_name='fbouser',
            name='medical_date',
        ),
        migrations.RemoveField(
            model_name='fbouser',
            name='pilot',
        ),
        migrations.RemoveField(
            model_name='fbouser',
            name='restrictions',
        ),
        migrations.RemoveField(
            model_name='fbouser',
            name='student',
        ),
        migrations.AddField(
            model_name='fbouser',
            name='contractor',
            field=models.ForeignKey(verbose_name='Kontrahent', to='fin.Contractor', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pilot',
            name='fbouser',
            field=models.OneToOneField(verbose_name='Użytkownik', to='panel.FBOUser'),
        ),
        migrations.AddField(
            model_name='pdt',
            name='instr',
            field=models.ForeignKey(verbose_name='Instruktor nadzorujący', related_name='pdt_instr_set', to='panel.Pilot', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pdt',
            name='pic',
            field=models.ForeignKey(verbose_name='Pierwszy pilot', to='panel.Pilot'),
        ),
        migrations.AddField(
            model_name='pdt',
            name='sic',
            field=models.ForeignKey(verbose_name='Drugi pilot', related_name='pdt_sic_set', to='panel.Pilot', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='operation',
            name='pdt',
            field=models.ForeignKey(to='panel.PDT'),
        ),
        migrations.AddField(
            model_name='duty',
            name='pilot',
            field=models.ForeignKey(to='panel.Pilot'),
        ),
    ]
