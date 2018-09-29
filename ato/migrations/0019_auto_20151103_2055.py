# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ato', '0018_auto_20151103_2054'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='module',
            options={'permissions': (('ato_admin', 'Dostęp do zarządzania szkoleniami'), ('ato_instructor', 'Dostęp do narzędzi instruktora'), ('ato_student', 'Dostęp do narzędzi ucznia'))},
        ),
    ]
