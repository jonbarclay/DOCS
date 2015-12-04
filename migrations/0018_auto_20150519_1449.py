# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DOCS', '0017_auto_20150519_1251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finding',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('finding_date', models.DateTimeField(verbose_name='date entered')),
                ('finding_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='requirement',
            name='finding_text',
        ),
        migrations.AddField(
            model_name='finding',
            name='requirement',
            field=models.ForeignKey(null=True, to='DOCS.Requirement', blank=True),
        ),
    ]
