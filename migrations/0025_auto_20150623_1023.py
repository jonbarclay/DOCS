# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DOCS', '0024_auto_20150617_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirement',
            name='expire_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='requirement',
            name='expire_days',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requirement',
            name='finding_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date entered'),
        ),
        migrations.AddField(
            model_name='requirement',
            name='finding_text',
            field=models.CharField(blank=True, null=True, max_length=200),
        ),
        migrations.AddField(
            model_name='requirement',
            name='req_repeat_status',
            field=models.CharField(default='Annually', choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Quarterly', 'Quarterly'), ('Semiannually', 'Semiannually'), ('Annually', 'Annually')], max_length=20),
        ),
        migrations.AlterField(
            model_name='requirement',
            name='req_status',
            field=models.CharField(default='Not In Place', choices=[('In Place', 'In Place'), ('Not In Place', 'Not In Place'), ('In Progress', 'In Progress'), ('Expired', 'Expired')], max_length=20),
        ),
    ]
