# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0019_auto_20160319_1358'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='module',
            options={'permissions': [('sms_reader', 'SMS - Dostęp do odczytu'), ('sms_admin', 'SMS - Dostęp pełny')]},
        ),
    ]
