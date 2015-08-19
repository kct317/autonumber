# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('autonumber', '0002_auto_20150821_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('databasename', models.CharField(default='', max_length=30)),
                ('databaseip', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Dba',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('username', models.CharField(default='', max_length=30)),
                ('first_name', models.CharField(default='', max_length=30)),
                ('last_name', models.CharField(default='', max_length=30)),
                ('email', models.EmailField(default='', max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('username', models.CharField(default='', max_length=30)),
                ('first_name', models.CharField(default='', max_length=30)),
                ('last_name', models.CharField(default='', max_length=30)),
                ('email', models.EmailField(default='', max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('statename', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('sql', models.CharField(null=True, blank=True, max_length=2000)),
                ('desc', models.CharField(null=True, blank=True, max_length=2000)),
                ('createdtime', models.DateTimeField()),
                ('lastupdatedtime', models.DateTimeField(null=True, blank=True)),
                ('dbacomment', models.CharField(null=True, blank=True, max_length=2000)),
                ('attachment', models.FileField(upload_to='tasks', null=True, blank=True)),
                ('creater', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('databases', models.ManyToManyField(to='autonumber.Database')),
                ('dba', models.ForeignKey(to='autonumber.Dba')),
                ('manager', models.ForeignKey(to='autonumber.Manager')),
                ('state', models.ForeignKey(to='autonumber.State')),
            ],
        ),
    ]
