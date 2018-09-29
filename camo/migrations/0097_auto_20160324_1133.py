# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0096_auto_20160308_0834'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='module',
            options={'permissions': [('camo_reader', 'CAMO - Dostęp do odczytu'), ('camo_admin', 'CAMO - Dostęp pełny')]},
        ),
    ]
