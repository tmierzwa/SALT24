# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ato', '0017_auto_20151103_2038'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='module',
            options={'permissions': (('ato_admin', 'Dostęp do zarządzania szkoleniami'), ('ato_instructor', 'Dostęp do narzędzi instruktora'), ('ato_student', 'Dostęp do narzędzi instruktora'))},
        ),
    ]
