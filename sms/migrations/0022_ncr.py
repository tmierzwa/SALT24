# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0021_smsreport_privacy'),
    ]

    operations = [
        migrations.CreateModel(
            name='NCR',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('audit_nbr', models.CharField(max_length=30, verbose_name='Numer audytu')),
                ('audit_date', models.DateField(verbose_name='Data audytu')),
                ('audit_type', models.CharField(choices=[('wewnętrzy', 'wewnętrzny'), ('zewnętrzny', 'zewnętrzny')], max_length=10, verbose_name='Rodzaj audytu')),
                ('audit_scope', models.CharField(choices=[('AOC/SPO', 'AOC/SPO'), ('CAMO', 'CAMO'), ('ATO', 'ATO')], max_length=10, verbose_name='Obszar audytu')),
                ('ncr_nbr', models.IntegerField(verbose_name='Numer NCR')),
                ('description', models.TextField(verbose_name='Treść NCR')),
                ('due_date', models.DateField(verbose_name='Wyznaczona data usunięcia')),
                ('done_date', models.DateField(blank=True, null=True, verbose_name='Data usunięcia')),
                ('check_date', models.DateField(blank=True, null=True, verbose_name='Data audytu sprawdzającego')),
            ],
        ),
    ]
