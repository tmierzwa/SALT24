# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0003_auto_20151127_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fbouser',
            name='module_ato',
            field=models.IntegerField(default=0, verbose_name='Moduł ATO', choices=[(0, 'Brak dostępu'), (1, 'Kierownik ATO'), (2, 'Pracownik ATO'), (3, 'Tylko odczyt')]),
        ),
        migrations.AlterField(
            model_name='fbouser',
            name='module_camo',
            field=models.IntegerField(default=0, verbose_name='Moduł CAMO', choices=[(0, 'Brak dostępu'), (1, 'Kierownik CAMO'), (2, 'Pracownik CAMO'), (3, 'Tylko odczyt')]),
        ),
        migrations.AlterField(
            model_name='fbouser',
            name='module_fin',
            field=models.IntegerField(default=0, verbose_name='Moduł finansowy', choices=[(0, 'Brak dostępu'), (1, 'Pełny dostęp')]),
        ),
        migrations.AlterField(
            model_name='fbouser',
            name='module_sms',
            field=models.IntegerField(default=0, verbose_name='Moduł SMS', choices=[(0, 'Brak dostępu'), (1, 'Pełny dostęp'), (2, 'Tylko odczyt')]),
        ),
    ]
