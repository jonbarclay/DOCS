# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DOCS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirement',
            name='req_status',
            field=models.CharField(choices=[('In Place', 'In Place'), ('Compensating Control', 'Compensating Control'), ('Not Applicable', 'Not Applicable'), ('Not Tested', 'Not Tested'), ('Not In Place', 'Not In Place')], max_length=20, default='Not In Place'),
        ),
    ]
