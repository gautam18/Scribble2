# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-27 08:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Entry', '0013_auto_20180327_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='entry_description',
            field=models.CharField(default='Empty', max_length=5000),
        ),
        migrations.AlterField(
            model_name='entry',
            name='entry_name',
            field=models.CharField(max_length=40),
        ),
    ]
