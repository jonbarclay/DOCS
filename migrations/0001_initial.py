# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guidance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('guidance_text', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('merchant_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Merchant_Rep_Finding',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('test_finding_text', models.CharField(max_length=200)),
                ('merchant', models.ForeignKey(to='DOCS.Merchant')),
            ],
        ),
        migrations.CreateModel(
            name='Merchant_Rep_Sub_Finding',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('test_finding_text', models.CharField(max_length=200)),
                ('merchant', models.ForeignKey(to='DOCS.Merchant')),
            ],
        ),
        migrations.CreateModel(
            name='Reporting_Instruction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rep_req_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Reporting_Sub_Instruction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rep_sub_text', models.CharField(max_length=200)),
                ('reporting_instruction', models.ForeignKey(to='DOCS.Reporting_Instruction')),
            ],
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('req_number', models.CharField(max_length=10)),
                ('req_text', models.CharField(max_length=200)),
                ('req_note', models.CharField(max_length=200, blank=True)),
                ('req_status', models.CharField(max_length=2, choices=[('IP', 'In Place'), ('CC', 'Compensating Control'), ('NA', 'Not Applicable'), ('NT', 'Not Tested'), ('NI', 'Not In Place')], default='NI')),
                ('merchant', models.ForeignKey(to='DOCS.Merchant')),
                ('parent_req', models.ForeignKey(null=True, related_name='child_req', blank=True, to='DOCS.Requirement')),
            ],
        ),
        migrations.CreateModel(
            name='Testing_Procedure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('test_number', models.CharField(max_length=10)),
                ('test_text', models.CharField(max_length=200)),
                ('requirement', models.ForeignKey(to='DOCS.Requirement')),
            ],
        ),
        migrations.CreateModel(
            name='Testing_Sub_Procedure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sub_test_text', models.CharField(max_length=200)),
                ('testing_procedure', models.ForeignKey(to='DOCS.Testing_Procedure')),
            ],
        ),
        migrations.AddField(
            model_name='reporting_instruction',
            name='testing_procedure',
            field=models.ForeignKey(to='DOCS.Testing_Procedure'),
        ),
        migrations.AddField(
            model_name='merchant_rep_sub_finding',
            name='reporting_sub_instruction',
            field=models.ForeignKey(to='DOCS.Reporting_Sub_Instruction'),
        ),
        migrations.AddField(
            model_name='merchant_rep_finding',
            name='reporting_instruction',
            field=models.ForeignKey(to='DOCS.Reporting_Instruction'),
        ),
        migrations.AddField(
            model_name='guidance',
            name='requirement',
            field=models.ForeignKey(to='DOCS.Requirement'),
        ),
    ]
