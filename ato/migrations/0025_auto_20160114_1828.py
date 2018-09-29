# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0007_pilot_remarks'),
        ('ato', '0024_auto_20160114_1818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='fbouser',
        ),
        migrations.RemoveField(
            model_name='student',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
        migrations.RemoveField(
            model_name='student',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='pesel',
        ),
        migrations.RemoveField(
            model_name='student',
            name='telephone',
        ),
        migrations.AddField(
            model_name='instructor',
            name='pilot',
            field=models.OneToOneField(default=1, verbose_name='Pilot', to='panel.Pilot'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='instructor',
            name='remarks',
            field=models.TextField(blank=True, null=True, verbose_name='Uwagi'),
        ),
        migrations.AddField(
            model_name='student',
            name='pilot',
            field=models.OneToOneField(default=1, verbose_name='Pilot', to='panel.Pilot'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='remarks',
            field=models.TextField(blank=True, null=True, verbose_name='Uwagi'),
        ),
    ]
