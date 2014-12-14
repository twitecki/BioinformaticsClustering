# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataclustering', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kluster',
            name='distanceMetric',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
