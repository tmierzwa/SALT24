# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0017_auto_20150804_2321'),
        ('camo', '0059_auto_20150804_2321'),
    ]

    operations = [
        migrations.CreateModel(
            name='SMSEvent',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('event_date', models.DateField(verbose_name='Data zdarzenia')),
                ('oper_type', models.CharField(max_length=10, choices=[('AOC', 'AOC'), ('ATO', 'ATO'), ('Wynajem', 'Wynajem'), ('Inne', 'Inne')], verbose_name='Rodzaj operacji')),
                ('event_type', models.CharField(max_length=10, choices=[('Incydent', 'Incydent'), ('Zdarzenie', 'Zdarzenie')], verbose_name='Kwalifikacja zdarzenia')),
                ('pkbwl_ref', models.CharField(max_length=10, null=True, blank=True, verbose_name='Numer ewidencyjny PKBWL')),
                ('pkwbl_date', models.DateField(null=True, blank=True, verbose_name='Data przyjęcia w PKBWL')),
                ('examiner', models.CharField(max_length=50, null=True, blank=True, verbose_name='Badający zdarzenie')),
                ('description', models.CharField(max_length=500, verbose_name='Skrócony opis zdarzenia')),
                ('scrutiny', models.CharField(max_length=500, null=True, blank=True, verbose_name='Przebieg badania wewnętrznego')),
                ('findings', models.CharField(max_length=500, null=True, blank=True, verbose_name='Wnioski i zalecenia po badaniu wewnętrznym')),
                ('closure', models.CharField(max_length=10, choices=[('---', '---'), ('Tak', 'Tak'), ('N/D', 'N/D')], verbose_name='Zamknięcie badania / raport końcowy')),
                ('remarks', models.CharField(max_length=500, null=True, blank=True, verbose_name='Uwagi')),
                ('aircraft', models.ForeignKey(to='camo.Aircraft')),
                ('pic', models.ForeignKey(to='pdt.Pilot')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SMSFailure',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('description', models.CharField(max_length=500, verbose_name='Skrócony opis usterki')),
                ('repair_date', models.DateField(null=True, blank=True, verbose_name='Data usunięcia usterki')),
                ('repair_desc', models.CharField(max_length=500, null=True, blank=True, verbose_name='Sposób usunięcia usterki')),
                ('findings', models.CharField(max_length=500, null=True, blank=True, verbose_name='Wnioski i zalecenia')),
                ('remarks', models.CharField(max_length=500, null=True, blank=True, verbose_name='Uwagi')),
                ('pdt_ref', models.ForeignKey(to='pdt.PDT')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SMSHazard',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('hazard_type', models.CharField(max_length=10, choices=[('Zewnętrzne', 'Zewnętrzne'), ('Osobowe', 'Osobowe'), ('Operacyjne', 'Operacyjne'), ('Techniczne', 'Techniczne'), ('Inne', 'Inne')], verbose_name='Klasa zagrożenia')),
                ('hazard_ref', models.CharField(max_length=10, verbose_name='Identyfikator zdarzenia')),
                ('hazard_date', models.DateField(verbose_name='Data wprowadzenia do rejestru')),
                ('company_area', models.CharField(max_length=10, choices=[('SALT', 'SALT'), ('ATO', 'ATO'), ('AOC', 'AOC'), ('Inne', 'Inne')], verbose_name='Obszar firmy')),
                ('name', models.CharField(max_length=100, verbose_name='Nazwa zagrożenia')),
                ('due_date', models.DateField(null=True, blank=True, verbose_name='Termin')),
                ('responsible', models.CharField(max_length=50, null=True, blank=True, verbose_name='Osoba odpowiedzialna')),
                ('control', models.CharField(max_length=100, null=True, blank=True, verbose_name='Wykonanie / kontrola')),
                ('remarks', models.CharField(max_length=500, null=True, blank=True, verbose_name='Uwagi')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SMSReport',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('report_date', models.DateField(verbose_name='Data zgłoszenia')),
                ('person', models.CharField(max_length=50, null=True, blank=True, verbose_name='Osoba zgłaszająca')),
                ('description', models.CharField(max_length=500, verbose_name='Skrócona treść zgłoszenia')),
                ('findings', models.CharField(max_length=500, null=True, blank=True, verbose_name='Wnioski i zalecenia')),
                ('remarks', models.CharField(max_length=500, null=True, blank=True, verbose_name='Uwagi')),
                ('smshazard', models.ForeignKey(null=True, blank=True, to='sms.SMSHazard', verbose_name='Zagrożenie w rejestrze')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SMSRisk',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('description', models.CharField(max_length=500, verbose_name='Szczegółowy opis natury ryzyka')),
                ('init_probability', models.CharField(max_length=1, choices=[('5', 'Bardzo wysokie'), ('4', 'Wysokie'), ('3', 'Średnie'), ('2', 'Niskie'), ('1', 'Bardzo niskie')], verbose_name='Początkowe prawdopodobieństwo')),
                ('init_impact', models.CharField(max_length=1, choices=[('E', 'Bardzo duża'), ('D', 'Duża'), ('C', 'Średnia'), ('B', 'Mała'), ('A', 'Bardzo mała')], verbose_name='Początkowa dotkliwość')),
                ('mitigation', models.CharField(max_length=500, null=True, blank=True, verbose_name='Sposoby ograniczania ryzyka')),
                ('res_probability', models.CharField(max_length=1, choices=[('5', 'Bardzo wysokie'), ('4', 'Wysokie'), ('3', 'Średnie'), ('2', 'Niskie'), ('1', 'Bardzo niskie')], blank=True, verbose_name='Szczątkowe prawdopodobieństwo', null=True)),
                ('res_impact', models.CharField(max_length=1, choices=[('E', 'Bardzo duża'), ('D', 'Duża'), ('C', 'Średnia'), ('B', 'Mała'), ('A', 'Bardzo mała')], blank=True, verbose_name='Szczątkowa dotkliwość', null=True)),
                ('smshazard', models.ForeignKey(to='sms.SMSHazard')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='smsfailure',
            name='smshazard',
            field=models.ForeignKey(null=True, blank=True, to='sms.SMSHazard', verbose_name='Zagrożenie w rejestrze'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='smsevent',
            name='smshazard',
            field=models.ForeignKey(null=True, blank=True, to='sms.SMSHazard', verbose_name='Zagrożenie w rejestrze'),
            preserve_default=True,
        ),
    ]
