# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0027_auto_20160324_1133'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('rating', models.CharField(max_length=50, verbose_name='Nazwa uprawnienia')),
                ('valid_date', models.DateField(blank=True, null=True, verbose_name='Ważność uprawnienia')),
                ('remarks', models.TextField(blank=True, null=True, verbose_name='Uwagi')),
            ],
        ),
        migrations.AlterField(
            model_name='fbouser',
            name='module_fin',
            field=models.IntegerField(choices=[(0, 'Brak dostępu'), (1, 'Tylko odczyt'), (2, 'Pełny dostęp')], default=0, verbose_name='Moduł FIN'),
        ),
        migrations.AlterField(
            model_name='pilot',
            name='employee',
            field=models.BooleanField(default=False, verbose_name='Kontrola czasu pracy'),
        ),
        migrations.AddField(
            model_name='ratings',
            name='pilot',
            field=models.ForeignKey(to='panel.Pilot', verbose_name='Pilot'),
        ),
    ]
