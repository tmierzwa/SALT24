# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0051_auto_20150712_1312'),
    ]

    operations = [
        migrations.CreateModel(
            name='PDT',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('pdt_ref', models.CharField(max_length=100, verbose_name='Numer PDT')),
                ('status', models.CharField(max_length=10, choices=[('open', 'Otwarty'), ('closed', 'Zamkni?ty')], default='open', verbose_name='Status')),
                ('aircraft', models.ForeignKey(to='camo.Aircraft')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pilot',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=100, verbose_name='Imi?')),
                ('nazwisko', models.CharField(max_length=100, verbose_name='Nazwisko')),
                ('licencja', models.CharField(max_length=100, verbose_name='Numer licencji')),
                ('upowaznienie', models.CharField(max_length=100, verbose_name='Numer upowa?nienia')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pdt',
            name='pic',
            field=models.ForeignKey(to='pdt.Pilot'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pdt',
            name='sic',
            field=models.ForeignKey(to='pdt.Pilot', related_name='PDT_sic_set'),
            preserve_default=True,
        ),
    ]
