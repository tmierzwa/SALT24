# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import salt.models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0039_auto_20160901_1045'),
        ('camo', '0101_auto_20160625_1205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('start_time', models.DateTimeField(verbose_name='Termin rozpoczęcia')),
                ('end_time', models.DateTimeField(verbose_name='Termin zakończenia')),
                ('planned_type', models.CharField(verbose_name='Planowany rodzaj lotu', null=True, blank=True, max_length=3, choices=[('01', '01 - Przewóz lotniczy'), ('01A', '01A - Lot widokowy'), ('02', '02 - Operacje specjal.'), ('02H', '02H - Operacje specjal. HR'), ('03A', '03A - Szkolenie AOC'), ('03B', '03B - Szkolenie ATO'), ('03C', '03C - Szkolenie SPO'), ('03D', '03D - Lot zapoznawczy'), ('03E', '03E - Lot egzaminacyjny'), ('04', '04 - Wynajem SP'), ('05', '05 - Loty niepłatne'), ('06', '06 - Oblot techniczny'), ('06A', '06A - Sprawdzenie SP'), ('07', '07 - Lot prywatny')])),
                ('planned_time', salt.models.MyDurationField(verbose_name='Planowany czas lotu', null=True, blank=True)),
                ('planned_route', models.CharField(verbose_name='Planowany czas lotu', null=True, blank=True, max_length=50)),
                ('remarks', models.TextField(verbose_name='Uwagi', null=True, blank=True)),
                ('internal_remarks', models.TextField(verbose_name='Uwagi SALT', null=True, blank=True)),
                ('status', models.CharField(choices=[('Nowa', 'Nowa'), ('Potwierdzona', 'Potwierdzona'), ('Zrealizowana', 'Zrealizowana'), ('Anulowana', 'Anulowana')], verbose_name='Status rezerwacji', max_length=12, default='Nowa')),
                ('open_time', models.DateTimeField(verbose_name='Termin otwarcia', auto_now_add=True)),
                ('change_time', models.DateTimeField(auto_now=True, verbose_name='Termin ostatniej modyfikacji')),
                ('aircraft', models.ForeignKey(to='camo.Aircraft', verbose_name='Statek powietrzny')),
                ('change_user', models.ForeignKey(to='panel.FBOUser', related_name='res_changed_by_set', blank=True, null=True, verbose_name='Zmodyfikowana przez')),
                ('open_user', models.ForeignKey(to='panel.FBOUser', verbose_name='Utworzona przez', related_name='res_open_by_set')),
                ('owner', models.ForeignKey(to='panel.Pilot', verbose_name='Właściciel rezerwacji', related_name='res_owner_set')),
                ('participant', models.ForeignKey(to='panel.Pilot', related_name='res_participant_set', blank=True, null=True, verbose_name='Uczestnik rezerwacji')),
            ],
        ),
    ]
