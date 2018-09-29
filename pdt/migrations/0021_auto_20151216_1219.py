# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdt', '0020_voucher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voucher',
            name='person',
        ),
        migrations.AddField(
            model_name='voucher',
            name='persons',
            field=models.IntegerField(default=1, verbose_name='Liczba osób'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='voucher',
            name='time',
            field=models.IntegerField(default=30, verbose_name='Czas trwania (min)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='voucher',
            name='voucher_code',
            field=models.CharField(default='', max_length=10, verbose_name='Kod vouchera'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='voucher',
            name='description',
            field=models.CharField(max_length=100, verbose_name='Opis vouchera'),
        ),
    ]
