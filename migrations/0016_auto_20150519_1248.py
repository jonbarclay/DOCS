# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DOCS', '0015_auto_20150519_1231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report_finding',
            name='testing_procedure',
        ),
        migrations.AddField(
            model_name='report_finding',
            name='requirement',
            field=models.ForeignKey(null=True, blank=True, to='DOCS.Requirement'),
        ),
    ]
