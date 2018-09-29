# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0002_auto_20151030_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fbouser',
            name='module_ato',
            field=models.IntegerField(verbose_name='Moduł ATO', default=0, choices=[(0, 'Brak dostępu do modułu'), (1, 'Pełny dostęp do modułu')]),
        ),
        migrations.AlterField(
            model_name='fbouser',
            name='module_camo',
            field=models.IntegerField(verbose_name='Moduł CAMO', default=0, choices=[(0, 'Brak dostępu do modułu'), (1, 'Pełny dostęp do modułu')]),
        ),
        migrations.AlterField(
            model_name='fbouser',
            name='module_fin',
            field=models.IntegerField(verbose_name='Moduł finansowy', default=0, choices=[(0, 'Brak dostępu do modułu'), (1, 'Pełny dostęp do modułu')]),
        ),
        migrations.AlterField(
            model_name='fbouser',
            name='module_sms',
            field=models.IntegerField(verbose_name='Moduł SMS', default=0, choices=[(0, 'Brak dostępu do modułu'), (1, 'Pełny dostęp do modułu')]),
        ),
    ]
