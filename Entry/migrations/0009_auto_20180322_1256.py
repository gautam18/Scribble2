# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-22 12:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Entry', '0008_auto_20180322_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='entry_release_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 22, 12, 56, 49, 653186)),
        ),
    ]
