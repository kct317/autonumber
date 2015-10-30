# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('username', models.CharField(db_index=True, max_length=40, unique=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('casename', models.CharField(max_length=128, default='')),
                ('caseproperty', models.IntegerField(default=0)),
                ('casecreater', models.CharField(max_length=128, default='')),
                ('documentunit', models.IntegerField(default=0)),
                ('documenttype', models.IntegerField(default=0)),
                ('litigant', models.CharField(max_length=30, default='')),
                ('litiganttype', models.IntegerField(default=0)),
                ('casevalue', models.IntegerField(default=0)),
                ('fines', models.IntegerField(default=0)),
                ('forfeituremoney', models.IntegerField(default=0)),
                ('forfeitureitem', models.CharField(max_length=128, default='')),
                ('forfeitureamount', models.IntegerField(default=0)),
                ('illegalfacts', models.TextField(default='')),
                ('law', models.TextField(default='')),
                ('punishbasis', models.TextField(default='')),
                ('createdate', models.DateTimeField()),
                ('informdate', models.DateTimeField()),
                ('informnumber', models.CharField(max_length=128, default='')),
                ('issueddate', models.DateTimeField()),
                ('decisionnumber', models.CharField(max_length=128, default='')),
                ('handlingunit', models.CharField(max_length=128, default='')),
                ('auditorman', models.CharField(max_length=30, default='')),
                ('remarkman', models.TextField(default='')),
                ('creater', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PermissionList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RoleList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('permission', models.ManyToManyField(to='autonumber.PermissionList')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ForeignKey(null=True, to='autonumber.RoleList', blank=True),
        ),
    ]
