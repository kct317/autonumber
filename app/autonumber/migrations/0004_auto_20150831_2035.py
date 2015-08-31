# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autonumber', '0003_database_dba_manager_state_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='documenttype',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='case',
            name='documentunit',
            field=models.IntegerField(default=0),
        ),
    ]
