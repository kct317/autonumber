# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('caseid', models.AutoField(primary_key=True, serialize=False)),
                ('casename', models.CharField(max_length=128, default='')),
                ('documentunit', models.IntegerField(default=0)),
                ('documenttype', models.IntegerField(default=0)),
                ('litigant', models.CharField(max_length=30, default='')),
                ('litiganttype', models.IntegerField(default=0)),
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
            name='CaseProperty',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('caseproname', models.CharField(max_length=128, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('databasename', models.CharField(max_length=30, default='')),
                ('databaseip', models.CharField(max_length=30, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Dba',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30, default='')),
                ('first_name', models.CharField(max_length=30, default='')),
                ('last_name', models.CharField(max_length=30, default='')),
                ('email', models.EmailField(max_length=70, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30, default='')),
                ('first_name', models.CharField(max_length=30, default='')),
                ('last_name', models.CharField(max_length=30, default='')),
                ('email', models.EmailField(max_length=70, default='')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('statename', models.CharField(max_length=20, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sql', models.CharField(max_length=2000, blank=True, null=True)),
                ('desc', models.CharField(max_length=2000, blank=True, null=True)),
                ('createdtime', models.DateTimeField()),
                ('lastupdatedtime', models.DateTimeField(blank=True, null=True)),
                ('dbacomment', models.CharField(max_length=2000, blank=True, null=True)),
                ('attachment', models.FileField(blank=True, upload_to='tasks', null=True)),
                ('creater', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('databases', models.ManyToManyField(to='autonumber.Database')),
                ('dba', models.ForeignKey(to='autonumber.Dba')),
                ('manager', models.ForeignKey(to='autonumber.Manager')),
                ('state', models.ForeignKey(to='autonumber.State')),
            ],
        ),
        migrations.AddField(
            model_name='case',
            name='caseproperty',
            field=models.ForeignKey(to='autonumber.CaseProperty'),
        ),
        migrations.AddField(
            model_name='case',
            name='creater',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
