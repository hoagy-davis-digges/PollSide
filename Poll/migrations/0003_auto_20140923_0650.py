# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Poll', '0002_auto_20140922_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='pollster',
            name='poll_home',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='poll',
            name='date',
            field=models.DateField(default=datetime.datetime(2014, 9, 23, 6, 50, 0, 751718)),
        ),
    ]
