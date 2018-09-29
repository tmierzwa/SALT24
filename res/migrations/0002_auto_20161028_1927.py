# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('res', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('module', models.BooleanField()),
            ],
            options={
                'permissions': [('res_user', 'REZERWACJE - Dostęp do modułu'), ('res_admin', 'REZERWACJE - Zarządzanie')],
            },
        ),
        migrations.AlterField(
            model_name='reservation',
            name='planned_route',
            field=models.CharField(blank=True, null=True, verbose_name='Planowana trasa lotu', max_length=50),
        ),
    ]
