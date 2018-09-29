# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ato', '0035_auto_20160317_1608'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='module',
            options={'permissions': [('ato_reader', 'ATO - Dostęp do odczytu'), ('ato_admin', 'ATO - Dostęp pełny')]},
        ),
    ]
