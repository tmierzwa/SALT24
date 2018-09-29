# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ato', '0016_auto_20151025_1834'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='module',
            options={'permissions': (('access_module', 'Dostęp do modułu szkoleń'), ('instructor', 'Dostęp do narzędzi instruktora'))},
        ),
    ]
