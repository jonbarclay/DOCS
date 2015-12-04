# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DOCS', '0002_auto_20150511_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchant',
            name='saq_req',
            field=models.CharField(choices=[('A', 'SAQ A'), ('A-EP', 'SAQ A-EP'), ('B', 'SAQ B'), ('C', 'SAQ C'), ('C-VT', 'SAQ C-VT'), ('D', 'SAQ D'), ('P2PE', 'SAQ P2PE')], default='D', max_length=4),
        ),
    ]
