# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('caseid', models.AutoField(serialize=False, primary_key=True)),
                ('casename', models.CharField(max_length=128, default='')),
                ('litigant', models.CharField(max_length=30, default='')),
                ('litiganttype', models.IntegerField(default=0)),
                ('caseproperty', models.IntegerField(default=0)),
                ('casevalue', models.IntegerField(default=0)),
                ('fines', models.IntegerField(default=0)),
                ('forfeituremoney', models.IntegerField(default=0)),
                ('forfeitureitem', models.CharField(max_length=128, default='')),
                ('forfeitureamount', models.IntegerField(default='')),
                ('illegalfacts', models.TextField(default='')),
                ('law', models.TextField(default='')),
                ('punishbasis', models.TextField(default='')),
                ('createdate', models.IntegerField(default=0)),
                ('informdate', models.IntegerField(default=0)),
                ('informnumber', models.CharField(max_length=128, default='')),
                ('issueddate', models.IntegerField(default=0)),
                ('decisionnumber', models.CharField(max_length=128, default='')),
                ('handlingunit', models.CharField(max_length=128, default='')),
                ('auditorman', models.CharField(max_length=30, default='')),
                ('remarkman', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(serialize=False, primary_key=True)),
                ('gid', models.IntegerField(default=0)),
                ('username', models.CharField(max_length=50, default='')),
                ('password', models.CharField(max_length=50, default='')),
                ('superman', models.BooleanField(default=False)),
                ('lastip', models.CharField(max_length=50, default='')),
                ('createtime', models.IntegerField(default=0)),
                ('updatetime', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('gid', models.AutoField(serialize=False, primary_key=True)),
                ('groupname', models.CharField(max_length=50, default='')),
                ('power', models.IntegerField(default=0)),
                ('createtime', models.IntegerField(default=0)),
                ('updatetime', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserLog',
            fields=[
                ('logid', models.AutoField(serialize=False, primary_key=True)),
                ('uid', models.IntegerField(default=0)),
                ('username', models.CharField(max_length=50, default='')),
                ('msg', models.TextField(default='')),
                ('ip', models.CharField(max_length=50, default='')),
                ('createtime', models.IntegerField(default=0)),
            ],
        ),
    ]
