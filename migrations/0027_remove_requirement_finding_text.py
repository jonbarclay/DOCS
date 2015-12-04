# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DOCS', '0026_auto_20150623_1032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requirement',
            name='finding_text',
        ),
    ]
