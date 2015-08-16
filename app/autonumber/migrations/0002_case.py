# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autonumber', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('caseid', models.AutoField(serialize=False, primary_key=True)),
                ('casename', models.CharField(default='', max_length=128)),
                ('litigant', models.CharField(default='', max_length=30)),
                ('litiganttype', models.IntegerField(default=0)),
                ('caseproperty', models.IntegerField(default=0)),
                ('casevalue', models.IntegerField(default=0)),
                ('fines', models.IntegerField(default=0)),
                ('forfeituremoney', models.IntegerField(default=0)),
                ('forfeitureitem', models.CharField(default='', max_length=128)),
                ('forfeitureamount', models.IntegerField(default='')),
                ('illegalfacts', models.TextField(default='')),
                ('law', models.TextField(default='')),
                ('punishbasis', models.TextField(default='')),
                ('createdate', models.IntegerField(default=0)),
                ('informdate', models.IntegerField(default=0)),
                ('informnumber', models.CharField(default='', max_length=128)),
                ('issueddate', models.IntegerField(default=0)),
                ('decisionnumber', models.CharField(default='', max_length=128)),
                ('handlingunit', models.CharField(default='', max_length=128)),
                ('auditorman', models.CharField(default='', max_length=30)),
                ('remarkman', models.TextField(default='')),
            ],
        ),
    ]
