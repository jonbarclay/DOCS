# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DOCS', '0014_auto_20150519_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report_finding',
            name='testing_procedure',
            field=models.ForeignKey(to='DOCS.Testing_Procedure'),
        ),
    ]
