# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0028_auto_20150404_2052'),
    ]

    operations = [
        migrations.CreateModel(
            name='modification',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('description', models.CharField(verbose_name='Opis', max_length=200)),
                ('done_date', models.DateField(verbose_name='Data wykonania')),
                ('done_hours', models.DecimalField(verbose_name='TTH wykonania', max_digits=6, decimal_places=1)),
                ('done_crs', models.CharField(verbose_name='Numer CRS', max_length=20)),
                ('remarks', models.CharField(verbose_name='Uwagi', max_length=500)),
                ('aircraft', models.ForeignKey(verbose_name='Statek powietrzny', to='camo.Aircraft')),
                ('aso', models.ForeignKey(verbose_name='Organizacja', to='camo.ASO')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='wb_report',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('description', models.CharField(verbose_name='Opis', max_length=200)),
                ('doc_ref', models.CharField(verbose_name='Numer dokumentu', max_length=20)),
                ('mass_change', models.DecimalField(verbose_name='Zmiana masy', max_digits=6, decimal_places=2)),
                ('empty_weight', models.DecimalField(verbose_name='Empty weight', max_digits=6, decimal_places=2)),
                ('lon_cg', models.DecimalField(verbose_name='Longitudal C.G.', max_digits=6, decimal_places=2)),
                ('lat_cg', models.DecimalField(verbose_name='Lateral C.G.', max_digits=6, decimal_places=2)),
                ('lon_moment', models.DecimalField(verbose_name='Longitudal moment', max_digits=6, decimal_places=2)),
                ('lat_moment', models.DecimalField(verbose_name='Lateral moment', max_digits=6, decimal_places=2)),
                ('done_date', models.DateField(verbose_name='Data wykonania')),
                ('done_hours', models.DecimalField(verbose_name='TTH wykonania', max_digits=6, decimal_places=1)),
                ('done_doc', models.CharField(verbose_name='Numer dokumentu', max_length=20)),
                ('remarks', models.CharField(verbose_name='Uwagi', max_length=500)),
                ('aircraft', models.ForeignKey(verbose_name='Statek powietrzny', to='camo.Aircraft')),
                ('aso', models.ForeignKey(verbose_name='Organizacja', to='camo.ASO')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='crs',
            name='done_date',
            field=models.DateField(default=datetime.date(2015, 4, 5)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='work_order',
            name='date',
            field=models.DateField(default=datetime.date(2015, 4, 5)),
            preserve_default=True,
        ),
    ]
