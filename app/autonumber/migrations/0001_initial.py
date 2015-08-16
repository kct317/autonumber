# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
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
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('groupname', models.CharField(max_length=50, default='')),
                ('power', models.IntegerField(default=0)),
                ('createtime', models.IntegerField(default=0)),
                ('updatetime', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserLog',
            fields=[
                ('logid', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.IntegerField(default=0)),
                ('username', models.CharField(max_length=50, default='')),
                ('msg', models.TextField(default='')),
                ('ip', models.CharField(max_length=50, default='')),
                ('createtime', models.IntegerField(default=0)),
            ],
        ),
    ]
