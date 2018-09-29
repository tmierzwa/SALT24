# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0016_remove_part_months_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work_order',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('number', models.CharField(max_length=25)),
                ('date', models.DateField(default=datetime.date(2015, 4, 1))),
                ('open', models.BooleanField(default=True)),
                ('done_date', models.DateField(null=True, blank=True)),
                ('done_hours', models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)),
                ('aircraft', models.ForeignKey(to='camo.Aircraft')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Work_order_line',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('done', models.BooleanField(default=False)),
                ('pot_group', models.ForeignKey(to='camo.POT_group')),
                ('work_order', models.ForeignKey(to='camo.Work_order')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
