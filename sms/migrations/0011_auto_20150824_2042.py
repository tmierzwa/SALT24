# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0010_auto_20150824_2039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='smsfailure',
            old_name='event_date',
            new_name='failure_date',
        ),
    ]
