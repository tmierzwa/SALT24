# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-06 12:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0040_fbouser_module_res'),
        ('camo', '0101_auto_20160625_1205'),
        ('res', '0002_auto_20161028_1927'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blackout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='Termin rozpoczęcia')),
                ('end_time', models.DateTimeField(verbose_name='Termin zakończenia')),
                ('remarks', models.TextField(blank=True, null=True, verbose_name='Uwagi')),
                ('open_time', models.DateTimeField(auto_now_add=True, verbose_name='Termin utworzenia')),
                ('aircraft', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='camo.Aircraft', verbose_name='Statek powietrzny')),
                ('open_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.FBOUser', verbose_name='Utworzone przez')),
            ],
        ),
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('Nowa', 'Nowa'), ('Potwierdzona', 'Potwierdzona'), ('Zrealizowana', 'Zrealizowana')], default='Nowa', max_length=12, verbose_name='Status rezerwacji'),
        ),
    ]
