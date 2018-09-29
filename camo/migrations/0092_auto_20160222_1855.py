# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0011_auto_20160221_1123'),
        ('camo', '0091_auto_20160221_1529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='camo_operation',
            name='pdt_operation',
        ),
        migrations.RemoveField(
            model_name='camo_operation',
            name='pdt_ref',
        ),
        migrations.AddField(
            model_name='camo_operation',
            name='pdt',
            field=models.OneToOneField(blank=True, verbose_name='Powiązany PDT', null=True, to='panel.PDT'),
        ),
    ]
