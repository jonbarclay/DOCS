# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DOCS', '0005_auto_20150513_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchant_rep_sub_finding',
            name='test_finding_text',
            field=models.CharField(max_length=10000),
        ),
    ]
