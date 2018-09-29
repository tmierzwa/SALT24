# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ato', '0006_instructor_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='license',
            field=models.CharField(verbose_name='Numer licencji', default='', max_length=20),
            preserve_default=False,
        ),
    ]
