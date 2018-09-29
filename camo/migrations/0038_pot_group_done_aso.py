# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camo', '0037_auto_20150409_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='pot_group',
            name='done_aso',
            field=models.ForeignKey(to='camo.ASO', default=1),
            preserve_default=False,
        ),
    ]
