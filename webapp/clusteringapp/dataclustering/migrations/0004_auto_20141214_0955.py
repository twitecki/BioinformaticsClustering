# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataclustering', '0003_auto_20141214_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kluster',
            name='user',
            field=models.ForeignKey(default=None, to='dataclustering.KlusterUser', null=True),
            preserve_default=True,
        ),
    ]
