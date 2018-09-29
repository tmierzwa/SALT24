# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0036_auto_20160815_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fbouser',
            name='module_sms',
            field=models.IntegerField(default=0, choices=[(0, 'Brak dostępu'), (1, 'Tylko odczyt'), (2, 'Pełen dostęp'), (3, 'Dostęp NCR')], verbose_name='Moduł SMS'),
        ),
    ]
