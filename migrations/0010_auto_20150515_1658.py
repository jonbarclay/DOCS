# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DOCS', '0009_auto_20150515_1648'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report_finding',
            old_name='testing_procedure',
            new_name='reporting_instruction',
        ),
    ]
