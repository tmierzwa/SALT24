# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0026_auto_20160321_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duty',
            name='block_time',
            field=models.DurationField(blank=True, null=True, verbose_name='Czas służby'),
        ),
        migrations.AlterField(
            model_name='duty',
            name='block_time_from',
            field=models.TimeField(blank=True, null=True, verbose_name='Rozpoczęcie służby'),
        ),
        migrations.AlterField(
            model_name='duty',
            name='block_time_to',
            field=models.TimeField(blank=True, null=True, verbose_name='Zakończenie służby'),
        ),
        migrations.AlterField(
            model_name='duty',
            name='duty_time_from',
            field=models.TimeField(blank=True, null=True, verbose_name='Rozpoczęcie pracy'),
        ),
        migrations.AlterField(
            model_name='duty',
            name='duty_time_to',
            field=models.TimeField(blank=True, null=True, verbose_name='Zakończenie pracy'),
        ),
        migrations.AlterField(
            model_name='fbouser',
            name='module_ato',
            field=models.IntegerField(verbose_name='Moduł ATO', default=0, choices=[(0, 'Brak dostępu'), (1, 'Tylko odczyt'), (2, 'Pełen dostęp')]),
        ),
        migrations.AlterField(
            model_name='fbouser',
            name='module_camo',
            field=models.IntegerField(verbose_name='Moduł CAMO', default=0, choices=[(0, 'Brak dostępu'), (1, 'Tylko odczyt'), (2, 'Pełen dostęp')]),
        ),
        migrations.AlterField(
            model_name='fbouser',
            name='module_fin',
            field=models.IntegerField(verbose_name='Moduł finansowy', default=0, choices=[(0, 'Brak dostępu'), (1, 'Tylko odczyt'), (2, 'Pełny dostęp')]),
        ),
        migrations.AlterField(
            model_name='fbouser',
            name='module_sms',
            field=models.IntegerField(verbose_name='Moduł SMS', default=0, choices=[(0, 'Brak dostępu'), (1, 'Tylko odczyt'), (2, 'Pełen dostęp')]),
        ),
    ]
