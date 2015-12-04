# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DOCS', '0019_auto_20150521_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirement',
            name='req_status',
            field=models.CharField(max_length=20, choices=[('In Place', 'In Place'), ('Not In Place', 'Not In Place'), ('In Progress', 'In Progress')], default='Not In Place'),
        ),
    ]
