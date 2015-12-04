# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DOCS', '0004_auto_20150513_0755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guidance',
            name='requirement',
        ),
        migrations.AddField(
            model_name='requirement',
            name='guidance_text',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.DeleteModel(
            name='Guidance',
        ),
    ]
