# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fin', '0017_auto_20160320_0951'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='module',
            options={'permissions': [('fin_reader', 'FIN - Dostęp do odczytu'), ('fin_admin', 'FIN - Dostęp pełny')]},
        ),
    ]
