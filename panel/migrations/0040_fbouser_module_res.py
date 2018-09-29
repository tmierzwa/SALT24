# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0039_auto_20160901_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='fbouser',
            name='module_res',
            field=models.IntegerField(choices=[(0, 'Brak dostępu'), (1, 'Tworzenie'), (2, 'Zarządzanie')], default=1, verbose_name='Moduł RES'),
        ),
    ]
