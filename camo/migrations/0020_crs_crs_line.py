# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0019_work_order_aso'),
    ]

    operations = [
        migrations.CreateModel(
            name='CRS',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('number', models.CharField(max_length=20)),
                ('done_date', models.DateField(default=datetime.date(2015, 4, 3))),
                ('done_hours', models.DecimalField(max_digits=6, decimal_places=1)),
                ('done_landings', models.IntegerField()),
                ('work_order', models.ForeignKey(to='camo.Work_order')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CRS_line',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('done', models.BooleanField(default=False)),
                ('crs', models.ForeignKey(to='camo.CRS')),
                ('pot_event', models.ForeignKey(to='camo.POT_event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
