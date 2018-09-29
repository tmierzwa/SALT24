# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0009_auto_20150325_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('part_no', models.CharField(max_length=30)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField(null=True, blank=True)),
                ('from_hours', models.IntegerField(default=0)),
                ('to_hours', models.IntegerField(null=True, blank=True)),
                ('current', models.BooleanField(default=False)),
                ('aircraft', models.ForeignKey(to='camo.Aircraft')),
                ('ata', models.ForeignKey(to='camo.ATA')),
                ('part', models.ForeignKey(to='camo.Part')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='item_as_part',
            name='item',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.RemoveField(
            model_name='item_as_part',
            name='part',
        ),
        migrations.DeleteModel(
            name='Item_as_part',
        ),
        migrations.RenameField(
            model_name='aircraft',
            old_name='ac_type',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='part',
            old_name='part_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='part',
            name='aircraft',
        ),
        migrations.RemoveField(
            model_name='part',
            name='part_no',
        ),
        migrations.RemoveField(
            model_name='part',
            name='super_part',
        ),
        migrations.AddField(
            model_name='part',
            name='hours_adjustment',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='part',
            name='hours_count',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='part',
            name='hours_start',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='part',
            name='install_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 30, 15, 21, 53, 950995, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='part',
            name='landings_adjustment',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='part',
            name='landings_count',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='part',
            name='landings_start',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='part',
            name='maker',
            field=models.CharField(max_length=100, default='Diamond'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='part',
            name='months_adjustment',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='part',
            name='months_count',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='part',
            name='months_start',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='part',
            name='production_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 30, 15, 22, 29, 25001, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='part',
            name='serial_no',
            field=models.CharField(max_length=30, default='1234'),
            preserve_default=False,
        ),
    ]
