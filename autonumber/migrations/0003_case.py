# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autonumber', '0002_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('casename', models.CharField(max_length=128)),
                ('litigant', models.CharField(max_length=30)),
                ('litiganttype', models.IntegerField()),
                ('caseproperty', models.IntegerField()),
                ('casevalue', models.IntegerField()),
                ('fines', models.IntegerField()),
                ('forfeituremoney', models.IntegerField()),
                ('forfeitureitem', models.CharField(max_length=128)),
                ('forfeitureamount', models.IntegerField()),
                ('illegalfacts', models.TextField()),
                ('law', models.TextField()),
                ('punishbasis', models.TextField()),
                ('createdate', models.DateField()),
                ('informdate', models.DateField()),
                ('informnumber', models.CharField(max_length=128)),
                ('issueddate', models.DateField()),
                ('decisionnumber', models.CharField(max_length=128)),
                ('handlingunit', models.CharField(max_length=128)),
                ('auditorman', models.CharField(max_length=30)),
                ('remarkman', models.TextField()),
            ],
        ),
    ]
