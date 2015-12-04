# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DOCS', '0006_auto_20150513_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='merchant_rep_sub_finding',
            name='merchant',
        ),
        migrations.RemoveField(
            model_name='merchant_rep_sub_finding',
            name='reporting_sub_instruction',
        ),
        migrations.RemoveField(
            model_name='reporting_sub_instruction',
            name='reporting_instruction',
        ),
        migrations.RemoveField(
            model_name='testing_sub_procedure',
            name='testing_procedure',
        ),
        migrations.DeleteModel(
            name='Merchant_Rep_Sub_Finding',
        ),
        migrations.DeleteModel(
            name='Reporting_Sub_Instruction',
        ),
        migrations.DeleteModel(
            name='Testing_Sub_Procedure',
        ),
    ]
