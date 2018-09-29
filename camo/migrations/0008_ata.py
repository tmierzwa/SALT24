# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0007_auto_20150323_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='ATA',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chapter', models.CharField(max_length=5)),
                ('chapter_title', models.CharField(max_length=100)),
                ('section', models.CharField(max_length=10)),
                ('section_title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
