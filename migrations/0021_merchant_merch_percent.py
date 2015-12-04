# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DOCS', '0020_auto_20150521_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchant',
            name='merch_percent',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
