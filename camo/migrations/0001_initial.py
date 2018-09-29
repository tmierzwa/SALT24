# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ac_type',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('maker_name', models.CharField(max_length=100)),
                ('type_code', models.CharField(max_length=12)),
                ('type_name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('registration', models.CharField(max_length=12)),
                ('serial_no', models.CharField(max_length=30)),
                ('production_date', models.DateField()),
                ('insurance_date', models.DateField(blank=True)),
                ('wb_date', models.DateField(blank=True)),
                ('arc_date', models.DateField(blank=True)),
                ('ac_type', models.ForeignKey(to='camo.Ac_type')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('maker_no', models.CharField(max_length=100)),
                ('serial_no', models.CharField(max_length=30)),
                ('item_name', models.CharField(max_length=200)),
                ('production_date', models.DateField()),
                ('location', models.PositiveSmallIntegerField(choices=[(1, 'Aircraft'), (2, 'Warehouse'), (3, 'Archive')], default=2)),
                ('hours_limit', models.IntegerField(blank=True)),
                ('hours_start', models.IntegerField(default=0)),
                ('hours_adjustment', models.IntegerField(default=0)),
                ('hours_tolerance', models.IntegerField(default=0)),
                ('hours_count', models.IntegerField(default=0)),
                ('months_limit', models.IntegerField(blank=True)),
                ('months_start', models.IntegerField(default=0)),
                ('months_adjustment', models.IntegerField(default=0)),
                ('months_tolerance', models.IntegerField(default=0)),
                ('months_count', models.IntegerField(default=0)),
                ('landings_limit', models.IntegerField(blank=True)),
                ('landings_start', models.IntegerField(default=0)),
                ('landings_adjustment', models.IntegerField(default=0)),
                ('landings_tolerance', models.IntegerField(default=0)),
                ('landings_count', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item_as_part',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField(blank=True)),
                ('from_hours', models.IntegerField()),
                ('to_hours', models.IntegerField(blank=True)),
                ('item', models.ForeignKey(to='camo.Item')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('pdt_ref', models.CharField(max_length=30)),
                ('operation_date', models.DateField()),
                ('operation_time', models.TimeField()),
                ('hours', models.IntegerField()),
                ('landings', models.IntegerField()),
                ('aircraft', models.ForeignKey(to='camo.Aircraft')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('part_no', models.CharField(max_length=30)),
                ('part_name', models.CharField(max_length=200)),
                ('aircraft', models.ForeignKey(to='camo.Aircraft')),
                ('super_part', models.ForeignKey(blank=True, to='camo.Part')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='item_as_part',
            name='part',
            field=models.ForeignKey(to='camo.Part'),
            preserve_default=True,
        ),
    ]
