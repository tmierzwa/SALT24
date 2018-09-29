# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0021_auto_20151216_1219'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Voucher',
        ),
    ]
