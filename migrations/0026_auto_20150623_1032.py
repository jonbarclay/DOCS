# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DOCS', '0025_auto_20150623_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirement',
            name='expire_days',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
