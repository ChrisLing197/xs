# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-02 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ys', '0006_auto_20170202_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='email',
            field=models.EmailField(default='', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='AccountID',
            field=models.CharField(default='', max_length=128, unique=True),
        ),
    ]
