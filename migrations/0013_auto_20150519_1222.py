# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DOCS', '0012_report_finding_testing_procedure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report_finding',
            name='testing_procedure',
            field=models.ForeignKey(to='DOCS.Testing_Procedure'),
        ),
    ]
