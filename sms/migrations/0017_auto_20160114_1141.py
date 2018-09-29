# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0016_auto_20160107_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smsfailure',
            name='pdt_ref',
            field=models.ForeignKey(verbose_name='Numer PDT', to='panel.PDT', blank=True, null=True),
        ),
    ]
