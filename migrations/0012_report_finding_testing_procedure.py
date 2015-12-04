# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DOCS', '0011_remove_report_finding_reporting_instruction'),
    ]

    operations = [
        migrations.AddField(
            model_name='report_finding',
            name='testing_procedure',
            field=models.ForeignKey(blank=True, to='DOCS.Testing_Procedure', null=True),
        ),
    ]
