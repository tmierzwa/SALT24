# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0006_auto_20150712_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('operation_no', models.IntegerField(verbose_name='Nr. rejsu', null=True, blank=True)),
                ('operation_type', models.CharField(verbose_name='Rodzaj lotu', max_length=3)),
                ('pax', models.IntegerField(verbose_name='Liczba pasa?erow', null=True, blank=True)),
                ('bags', models.IntegerField(verbose_name='Ci??ar bagazu [kg]', null=True, blank=True)),
                ('fuel_refill', models.IntegerField(verbose_name='Uzupe?nione paliwo', default=0)),
                ('fuel_available', models.IntegerField(verbose_name='Stan paliwa do lotu')),
                ('oil_lh_refill', models.DecimalField(verbose_name='Uzupe?niony olej', default=0, decimal_places=1, max_digits=3)),
                ('oil_rh_refill', models.DecimalField(verbose_name='Uzupe?niony olej RH', default=0, decimal_places=1, max_digits=3)),
                ('oil_state', models.CharField(verbose_name='Olej w normie', null=True, choices=[('ok', 'OK')], blank=True, max_length=3)),
                ('trans_oil_refill', models.DecimalField(verbose_name='Uzupe?niony olej przek?.', null=True, max_digits=3, decimal_places=1, blank=True, default=0)),
                ('trans_oil_state', models.CharField(verbose_name='Olej przek?. w normie', null=True, choices=[('ok', 'OK')], blank=True, max_length=3)),
                ('hydr_oil_refill', models.DecimalField(verbose_name='Uzupe?niony olej hydr.', null=True, max_digits=3, decimal_places=1, blank=True, default=0)),
                ('hydr_oil_state', models.CharField(verbose_name='Olej hydr. w normie', null=True, choices=[('ok', 'OK')], blank=True, max_length=3)),
                ('loc_start', models.CharField(verbose_name='Miejsce startu', max_length=20)),
                ('time_start', models.TimeField(verbose_name='Czas off-block')),
                ('tth_start', models.DecimalField(verbose_name='Licznik pocz?tkowy', max_digits=6, decimal_places=1)),
                ('loc_end', models.CharField(verbose_name='Miejsce l?dowania', max_length=20)),
                ('time_end', models.TimeField(verbose_name='Czas on-block')),
                ('tth_end', models.DecimalField(verbose_name='Licznik ko?cowy', max_digits=6, decimal_places=1)),
                ('landings', models.IntegerField(verbose_name='Liczba l?dowa?')),
                ('pdt', models.ForeignKey(to='pdt.PDT')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pdt',
            name='close_time',
            field=models.DateTimeField(verbose_name='Czas zamkni?cia', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pdt',
            name='n1_cycles',
            field=models.IntegerField(verbose_name='Liczba cykli N1', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pdt',
            name='n2_cycles',
            field=models.IntegerField(verbose_name='Liczba cykli N2', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pdt',
            name='open_time',
            field=models.DateTimeField(verbose_name='Czas otwarcia', default=datetime.datetime(2015, 7, 13, 20, 24, 38, 5412, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pdt',
            name='pic',
            field=models.ForeignKey(verbose_name='Pierwszy pilot', to='pdt.Pilot'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pdt',
            name='sic',
            field=models.ForeignKey(verbose_name='Drugi pilot', to='pdt.Pilot', null=True, related_name='pdt_sic_set', blank=True),
            preserve_default=True,
        ),
    ]
