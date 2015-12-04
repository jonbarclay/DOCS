# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DOCS', '0022_saq_saqreq'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saq',
            name='merchant',
        ),
        migrations.AddField(
            model_name='merchant',
            name='saq',
            field=models.ForeignKey(to='DOCS.SAQ', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='saqreq',
            name='saq',
            field=models.ForeignKey(to='DOCS.SAQ'),
        ),
    ]
