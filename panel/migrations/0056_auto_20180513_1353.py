# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-13 11:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import salt.models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0055_auto_20171129_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duty',
            name='duty_time',
            field=salt.models.MyDurationField(verbose_name=b'Czas \xc5\x82\xc4\x85czny'),
        ),
        migrations.AlterField(
            model_name='duty',
            name='duty_time_from',
            field=models.TimeField(verbose_name=b'Rozpocz\xc4\x99cie'),
        ),
        migrations.AlterField(
            model_name='duty',
            name='duty_time_to',
            field=models.TimeField(verbose_name=b'Zako\xc5\x84czenie'),
        ),
        migrations.AlterField(
            model_name='duty',
            name='duty_type',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name=b'Rodzaj obowi\xc4\x85zk\xc3\xb3w'),
        ),
        migrations.AlterField(
            model_name='duty',
            name='fdp_time',
            field=salt.models.MyDurationField(blank=True, null=True, verbose_name=b'Czas czynno\xc5\x9bci'),
        ),
        migrations.AlterField(
            model_name='duty',
            name='landings',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Liczba l\xc4\x85dowa\xc5\x84'),
        ),
        migrations.AlterField(
            model_name='duty',
            name='time_factor',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=3, verbose_name=b'Mno\xc5\xbcnik czasu'),
        ),
        migrations.AlterField(
            model_name='fbouser',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name=b'Imi\xc4\x99'),
        ),
        migrations.AlterField(
            model_name='fbouser',
            name='infos',
            field=models.BooleanField(default=False, verbose_name=b'Dost\xc4\x99p do INFOS'),
        ),
        migrations.AlterField(
            model_name='fbouser',
            name='module_ato',
            field=models.IntegerField(choices=[(0, b'Brak dost\xc4\x99pu'), (1, b'Tylko odczyt'), (2, b'Pe\xc5\x82en dost\xc4\x99p')], default=0, verbose_name=b'Modu\xc5\x82 ATO'),
        ),
        migrations.AlterField(
            model_name='fbouser',
            name='module_camo',
            field=models.IntegerField(choices=[(0, b'Brak dost\xc4\x99pu'), (1, b'Tylko odczyt'), (2, b'Pe\xc5\x82en dost\xc4\x99p')], default=0, verbose_name=b'Modu\xc5\x82 CAMO'),
        ),
        migrations.AlterField(
            model_name='fbouser',
            name='module_fin',
            field=models.IntegerField(choices=[(0, b'Brak dost\xc4\x99pu'), (1, b'Tylko odczyt'), (2, b'Pe\xc5\x82ny dost\xc4\x99p')], default=0, verbose_name=b'Modu\xc5\x82 FIN'),
        ),
        migrations.AlterField(
            model_name='fbouser',
            name='module_res',
            field=models.IntegerField(choices=[(0, b'Brak dost\xc4\x99pu'), (1, b'Tworzenie'), (2, b'Zarz\xc4\x85dzanie')], default=1, verbose_name=b'Modu\xc5\x82 RES'),
        ),
        migrations.AlterField(
            model_name='fbouser',
            name='module_sms',
            field=models.IntegerField(choices=[(0, b'Brak dost\xc4\x99pu'), (1, b'Tylko odczyt'), (2, b'Pe\xc5\x82en dost\xc4\x99p'), (3, b'Dost\xc4\x99p NCR')], default=0, verbose_name=b'Modu\xc5\x82 SMS'),
        ),
        migrations.AlterField(
            model_name='operation',
            name='bags',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Ci\xc4\x99\xc5\xbcar bagazu [kg]'),
        ),
        migrations.AlterField(
            model_name='operation',
            name='fuel_refill',
            field=models.IntegerField(default=0, verbose_name=b'Uzupe\xc5\x82nione paliwo (L)'),
        ),
        migrations.AlterField(
            model_name='operation',
            name='fuel_source',
            field=models.CharField(default=b'unknown', max_length=10, verbose_name=b'\xc5\xb9r\xc3\xb3d\xc5\x82o paliwa'),
        ),
        migrations.AlterField(
            model_name='operation',
            name='fuel_used',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Paliwo zu\xc5\xbcyte (L)'),
        ),
        migrations.AlterField(
            model_name='operation',
            name='landings',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name=b'Liczba l\xc4\x85dowa\xc5\x84'),
        ),
        migrations.AlterField(
            model_name='operation',
            name='loc_end',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name=b'Miejsce l\xc4\x85dowania'),
        ),
        migrations.AlterField(
            model_name='operation',
            name='oil_refill',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3, verbose_name=b'Uzupe\xc5\x82niony olej (qt)'),
        ),
        migrations.AlterField(
            model_name='operation',
            name='pax',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Liczba pasa\xc5\xbcerow'),
        ),
        migrations.AlterField(
            model_name='operation',
            name='status',
            field=models.CharField(choices=[(b'open', b'Otwarta'), (b'closed', b'Zamkni\xc4\x99ta')], default=b'open', max_length=10, verbose_name=b'Status'),
        ),
        migrations.AlterField(
            model_name='operation',
            name='trans_oil_refill',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=3, null=True, verbose_name=b'Uzup. olej przek\xc5\x82. (qt)'),
        ),
        migrations.AlterField(
            model_name='operation',
            name='tth_end',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name=b'Licznik ko\xc5\x84cowy'),
        ),
        migrations.AlterField(
            model_name='operation',
            name='tth_start',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name=b'Licznik pocz\xc4\x85tkowy'),
        ),
        migrations.AlterField(
            model_name='pdt',
            name='close_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name=b'Czas zamkni\xc4\x99cia'),
        ),
        migrations.AlterField(
            model_name='pdt',
            name='close_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pdt_closed_by_set', to='panel.FBOUser', verbose_name=b'Zamkni\xc4\x99ty przez'),
        ),
        migrations.AlterField(
            model_name='pdt',
            name='fuel_after_source',
            field=models.CharField(default=b'unknown', max_length=10, verbose_name=b'\xc5\xb9r\xc3\xb3d\xc5\x82o paliwa po locie'),
        ),
        migrations.AlterField(
            model_name='pdt',
            name='instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pdt_instr_set', to='panel.Pilot', verbose_name=b'Instruktor nadzoruj\xc4\x85cy'),
        ),
        migrations.AlterField(
            model_name='pdt',
            name='next_pdt',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prev_pdt', to='panel.PDT', verbose_name=b'Nast\xc4\x99pny PDT dla SP'),
        ),
        migrations.AlterField(
            model_name='pdt',
            name='prev_landings',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name=b'Suma l\xc4\x85dowa\xc5\x84 z przeniesienia'),
        ),
        migrations.AlterField(
            model_name='pdt',
            name='reapair_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pdt_repaired_by_set', to='panel.FBOUser', verbose_name=b'Usuni\xc4\x99ta przez'),
        ),
        migrations.AlterField(
            model_name='pdt',
            name='repair_desc',
            field=models.TextField(blank=True, null=True, verbose_name=b'Spos\xc3\xb3b usuni\xc4\x99cia'),
        ),
        migrations.AlterField(
            model_name='pdt',
            name='repair_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name=b'Czas usuni\xc4\x99cia'),
        ),
        migrations.AlterField(
            model_name='pdt',
            name='service_remarks',
            field=models.TextField(blank=True, null=True, verbose_name=b'Opis us\xc5\x82ugi'),
        ),
        migrations.AlterField(
            model_name='pdt',
            name='status',
            field=models.CharField(choices=[(b'open', b'Otwarty'), (b'closed', b'Zamkni\xc4\x99ty'), (b'checked', b'Sprawdzony')], default=b'open', max_length=10, verbose_name=b'Status'),
        ),
        migrations.AlterField(
            model_name='pdt',
            name='tth_start',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name=b'Licznik pocz\xc4\x85tkowy'),
        ),
        migrations.AlterField(
            model_name='pilot',
            name='clearance',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name=b'Upowa\xc5\xbcnienie SALT'),
        ),
        migrations.AlterField(
            model_name='pilot',
            name='fbouser',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='panel.FBOUser', verbose_name=b'U\xc5\xbcytkownik'),
        ),
        migrations.AlterField(
            model_name='pilot',
            name='licence_date',
            field=models.DateField(blank=True, null=True, verbose_name=b'Wa\xc5\xbcno\xc5\x9b\xc4\x87 licencji'),
        ),
        migrations.AlterField(
            model_name='pilot',
            name='medical_date',
            field=models.DateField(blank=True, null=True, verbose_name=b'Wa\xc5\xbcno\xc5\x9b\xc4\x87 bada\xc5\x84'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='valid_date',
            field=models.DateField(blank=True, null=True, verbose_name=b'Wa\xc5\xbcno\xc5\x9b\xc4\x87 uprawnienia'),
        ),
    ]