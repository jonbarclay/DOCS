# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DOCS', '0023_auto_20150522_1010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saqreq',
            name='saq',
        ),
        migrations.RemoveField(
            model_name='merchant',
            name='saq',
        ),
        migrations.DeleteModel(
            name='SAQ',
        ),
        migrations.DeleteModel(
            name='SAQReq',
        ),
    ]
