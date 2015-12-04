# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DOCS', '0021_merchant_merch_percent'),
    ]

    operations = [
        migrations.CreateModel(
            name='SAQ',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('saq_text', models.CharField(max_length=200)),
                ('merchant', models.ForeignKey(null=True, blank=True, to='DOCS.Merchant')),
            ],
        ),
        migrations.CreateModel(
            name='SAQReq',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('saqreq_text', models.CharField(max_length=200)),
                ('saq', models.ForeignKey(null=True, blank=True, to='DOCS.SAQ')),
            ],
        ),
    ]
