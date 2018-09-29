# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0022_ncr'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='module',
            options={'permissions': [('sms_reader', 'SMS - Dostęp do odczytu'), ('sms_ncr', 'SMS - Dostęp do NCR'), ('sms_admin', 'SMS - Dostęp pełny')]},
        ),
        migrations.AlterField(
            model_name='ncr',
            name='audit_type',
            field=models.CharField(max_length=10, choices=[('Wewnętrzny', 'Wewnętrzny'), ('Zewnętrzny', 'Zewnętrzny')], verbose_name='Rodzaj audytu'),
        ),
    ]
