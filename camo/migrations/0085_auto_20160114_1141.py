# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0084_auto_20160111_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camo_operation',
            name='pdt_operation',
            field=models.OneToOneField(to='panel.Operation', blank=True, null=True),
        ),
    ]
