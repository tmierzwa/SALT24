# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0005_item_as_part_current'),
    ]

    operations = [
        migrations.CreateModel(
            name='POT_event',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('POT_ref', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='POT_group',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('due_hours', models.IntegerField(blank=True, null=True)),
                ('due_months', models.IntegerField(blank=True, null=True)),
                ('due_landings', models.IntegerField(blank=True, null=True)),
                ('done_date', models.DateField(blank=True, null=True)),
                ('done_hours', models.IntegerField(blank=True, null=True)),
                ('done_months', models.IntegerField(blank=True, null=True)),
                ('done_landings', models.IntegerField(blank=True, null=True)),
                ('aircraft', models.ForeignKey(to='camo.Aircraft')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pot_event',
            name='POT_group',
            field=models.ForeignKey(to='camo.POT_group'),
            preserve_default=True,
        ),
    ]
