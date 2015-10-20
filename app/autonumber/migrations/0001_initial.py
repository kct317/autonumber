# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, verbose_name='last login', null=True)),
                ('username', models.CharField(max_length=40, db_index=True, unique=True)),
                ('email', models.EmailField(max_length=255)),
                ('is_active', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('nickname', models.CharField(max_length=64, null=True)),
                ('sex', models.CharField(max_length=2, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('caseid', models.AutoField(serialize=False, primary_key=True)),
                ('casename', models.CharField(max_length=128, default='')),
                ('casecreater', models.CharField(max_length=128, default='')),
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
                ('createdate', models.DateTimeField(default=datetime.datetime(2015, 10, 20, 11, 43, 9, 998623))),
                ('informdate', models.DateTimeField(default=datetime.datetime(2015, 10, 20, 11, 43, 9, 998623))),
                ('informnumber', models.CharField(max_length=128, default='')),
                ('issueddate', models.DateTimeField(default=datetime.datetime(2015, 10, 20, 11, 43, 9, 998623))),
                ('decisionnumber', models.CharField(max_length=128, default='')),
                ('handlingunit', models.CharField(max_length=128, default='')),
                ('auditorman', models.CharField(max_length=30, default='')),
                ('remarkman', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='CaseProperty',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('caseproname', models.CharField(max_length=128, default='')),
            ],
        ),
        migrations.CreateModel(
            name='PermissionList',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=64)),
                ('url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RoleList',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
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
            field=models.ForeignKey(blank=True, to='autonumber.RoleList', null=True),
        ),
    ]
