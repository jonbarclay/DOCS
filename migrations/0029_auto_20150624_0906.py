# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DOCS', '0028_auto_20150623_1209'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requirement',
            old_name='finding_date',
            new_name='completion_date',
        ),
    ]
