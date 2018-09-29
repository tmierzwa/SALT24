# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ato', '0020_auto_20160114_1141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='email',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='license',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='name',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='telephone',
        ),
        migrations.AlterField(
            model_name='instructor',
            name='user',
            field=models.OneToOneField(to='panel.FBOUser', verbose_name='Użytkownik'),
        ),
    ]
