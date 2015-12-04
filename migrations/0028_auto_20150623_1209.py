# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DOCS', '0027_remove_requirement_finding_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirement',
            name='finding_date',
            field=models.DateTimeField(blank=True, verbose_name='date completed', null=True),
        ),
    ]
