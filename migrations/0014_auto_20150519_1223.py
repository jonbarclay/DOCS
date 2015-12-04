# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DOCS', '0013_auto_20150519_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report_finding',
            name='testing_procedure',
            field=models.OneToOneField(to='DOCS.Testing_Procedure'),
        ),
    ]
