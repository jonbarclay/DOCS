# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DOCS', '0007_auto_20150515_0837'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report_Finding',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('test_finding_text', models.CharField(max_length=200)),
                ('reporting_instruction', models.ForeignKey(to='DOCS.Reporting_Instruction')),
            ],
        ),
        migrations.RemoveField(
            model_name='merchant_rep_finding',
            name='merchant',
        ),
        migrations.RemoveField(
            model_name='merchant_rep_finding',
            name='reporting_instruction',
        ),
        migrations.DeleteModel(
            name='Merchant_Rep_Finding',
        ),
    ]
