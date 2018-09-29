# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0094_auto_20160225_2205'),
        ('panel', '0016_auto_20160302_0948'),
    ]

    operations = [
        migrations.CreateModel(
            name='PilotAircraft',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('aircraft', models.ForeignKey(verbose_name='Statek powietrzny', to='camo.Aircraft')),
                ('pilot', models.ForeignKey(verbose_name='Pilot', to='panel.Pilot')),
            ],
        ),
        migrations.CreateModel(
            name='PilotFlightType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('flight_type', models.CharField(verbose_name='Rodzaj lotu', max_length=3)),
                ('pilot', models.ForeignKey(verbose_name='Pilot', to='panel.Pilot')),
            ],
        ),
        migrations.AlterField(
            model_name='operation',
            name='fuel_source',
            field=models.CharField(verbose_name='Źródło paliwa', default='unknown', max_length=10),
        ),
    ]
