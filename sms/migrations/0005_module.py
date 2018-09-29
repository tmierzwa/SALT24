# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0004_auto_20150813_1851'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('module', models.BooleanField()),
            ],
            options={
                'permissions': (('access_module', 'Dostęp do modułu SMS'),),
            },
        ),
    ]
