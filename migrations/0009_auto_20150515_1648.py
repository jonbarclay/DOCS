# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DOCS', '0008_auto_20150515_0916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report_finding',
            old_name='reporting_instruction',
            new_name='testing_procedure',
        ),
    ]
