# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ato', '0014_instructor_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='user',
            field=models.OneToOneField(verbose_name='Login', related_name='instructor', to=settings.AUTH_USER_MODEL),
        ),
    ]
