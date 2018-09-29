# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0028_auto_20160324_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('rating', models.CharField(max_length=50, verbose_name='Nazwa uprawnienia')),
                ('valid_date', models.DateField(verbose_name='Ważność uprawnienia', blank=True, null=True)),
                ('remarks', models.TextField(verbose_name='Uwagi', blank=True, null=True)),
                ('pilot', models.ForeignKey(verbose_name='Pilot', to='panel.Pilot')),
            ],
        ),
        migrations.RemoveField(
            model_name='ratings',
            name='pilot',
        ),
        migrations.DeleteModel(
            name='Ratings',
        ),
    ]
