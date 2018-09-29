# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-13 11:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('res', '0013_reservation_pax'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blackout',
            name='end_time',
            field=models.DateTimeField(verbose_name=b'Termin zako\xc5\x84czenia'),
        ),
        migrations.AlterField(
            model_name='blackout',
            name='start_time',
            field=models.DateTimeField(verbose_name=b'Termin rozpocz\xc4\x99cia'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='end_time',
            field=models.DateTimeField(verbose_name=b'Termin zako\xc5\x84czenia'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='res_owner_set', to='panel.Pilot', verbose_name=b'W\xc5\x82a\xc5\x9bciciel rezerwacji'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='pax',
            field=models.TextField(blank=True, null=True, verbose_name=b'Lista pasa\xc5\xbcer\xc3\xb3w'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='planned_type',
            field=models.CharField(choices=[(b'01', b'01 - Przew\xc3\xb3z lotniczy'), (b'01A', b'01A - Lot widokowy'), (b'02', b'02 - Operacje specjal.'), (b'02H', b'02H - Operacje specjal. HR'), (b'03A', b'03A - Szkolenie AOC'), (b'03B', b'03B - Szkolenie ATO'), (b'03C', b'03C - Szkolenie SPO'), (b'03D', b'03D - Lot zapoznawczy'), (b'03E', b'03E - Lot egzaminacyjny'), (b'04', b'04 - Wynajem SP'), (b'05', b'05 - Loty niep\xc5\x82atne'), (b'06', b'06 - Oblot techniczny'), (b'06A', b'06A - Sprawdzenie SP'), (b'07', b'07 - Lot prywatny')], max_length=3, verbose_name=b'Planowany rodzaj lotu'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='start_time',
            field=models.DateTimeField(verbose_name=b'Termin rozpocz\xc4\x99cia'),
        ),
        migrations.AlterField(
            model_name='reservationfbo',
            name='end_time',
            field=models.DateTimeField(verbose_name=b'Termin zako\xc5\x84czenia'),
        ),
        migrations.AlterField(
            model_name='reservationfbo',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resfbo_owner_set', to='panel.FBOUser', verbose_name=b'W\xc5\x82a\xc5\x9bciciel rezerwacji'),
        ),
        migrations.AlterField(
            model_name='reservationfbo',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='res.ResourceFBO', verbose_name=b'Rezerwowany zas\xc3\xb3b'),
        ),
        migrations.AlterField(
            model_name='reservationfbo',
            name='start_time',
            field=models.DateTimeField(verbose_name=b'Termin rozpocz\xc4\x99cia'),
        ),
        migrations.AlterField(
            model_name='reservationfbo',
            name='title',
            field=models.CharField(max_length=30, verbose_name=b'Tytu\xc5\x82 rezerwacji'),
        ),
        migrations.AlterField(
            model_name='resourcefbo',
            name='color',
            field=models.CharField(default=b'#cdcdcd', max_length=7, verbose_name=b'Kolor wy\xc5\x9bwietlania'),
        ),
        migrations.AlterField(
            model_name='resourcefbo',
            name='info',
            field=models.TextField(blank=True, null=True, verbose_name=b'Informacje dla u\xc5\xbcytkownk\xc3\xb3w'),
        ),
    ]