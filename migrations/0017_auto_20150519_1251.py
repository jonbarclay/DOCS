# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DOCS', '0016_auto_20150519_1248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report_finding',
            name='requirement',
        ),
        migrations.AddField(
            model_name='requirement',
            name='finding_text',
            field=models.CharField(max_length=10000, blank=True),
        ),
        migrations.DeleteModel(
            name='Report_Finding',
        ),
    ]
