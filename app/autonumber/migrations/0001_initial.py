# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('username', models.CharField(unique=True, max_length=40, db_index=True)),
                ('email', models.EmailField(max_length=255)),
                ('is_active', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('nickname', models.CharField(null=True, max_length=64)),
                ('sex', models.CharField(null=True, max_length=2)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('caseid', models.AutoField(primary_key=True, serialize=False)),
                ('casename', models.CharField(default='', max_length=128)),
                ('casecreater', models.CharField(default='', max_length=128)),
                ('documentunit', models.IntegerField(default=0)),
                ('documenttype', models.IntegerField(default=0)),
                ('litigant', models.CharField(default='', max_length=30)),
                ('litiganttype', models.IntegerField(default=0)),
                ('casevalue', models.IntegerField(default=0)),
                ('fines', models.IntegerField(default=0)),
                ('forfeituremoney', models.IntegerField(default=0)),
                ('forfeitureitem', models.CharField(default='', max_length=128)),
                ('forfeitureamount', models.IntegerField(default='')),
                ('illegalfacts', models.TextField(default='')),
                ('law', models.TextField(default='')),
                ('punishbasis', models.TextField(default='')),
                ('createdate', models.DateTimeField(default=datetime.datetime.now)),
                ('informdate', models.DateTimeField(default=datetime.datetime.now)),
                ('informnumber', models.CharField(default='', max_length=128)),
                ('issueddate', models.DateTimeField(default=datetime.datetime.now)),
                ('decisionnumber', models.CharField(default='', max_length=128)),
                ('handlingunit', models.CharField(default='', max_length=128)),
                ('auditorman', models.CharField(default='', max_length=30)),
                ('remarkman', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='CaseProperty',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('caseproname', models.CharField(default='', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='PermissionList',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RoleList',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('permission', models.ManyToManyField(to='autonumber.PermissionList')),
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
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ForeignKey(null=True, blank=True, to='autonumber.RoleList'),
        ),
    ]
