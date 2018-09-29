# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0066_auto_20150818_2036'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('module', models.BooleanField()),
            ],
            options={
                'permissions': (('access_module', 'Dostęp do modułu CAMO'),),
            },
        ),
        migrations.AlterModelOptions(
            name='aircraft',
            options={},
        ),
    ]
