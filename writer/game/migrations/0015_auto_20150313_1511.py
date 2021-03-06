# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0014_auto_20150313_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='classament',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='game',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 13, 15, 11, 52, 379091)),
            preserve_default=True,
        ),
    ]
