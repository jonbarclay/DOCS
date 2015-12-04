# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DOCS', '0003_merchant_saq_req'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirement',
            name='req_note',
            field=models.CharField(max_length=10000, blank=True),
        ),
    ]
