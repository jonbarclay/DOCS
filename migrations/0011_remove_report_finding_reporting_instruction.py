# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DOCS', '0010_auto_20150515_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report_finding',
            name='reporting_instruction',
        ),
    ]
