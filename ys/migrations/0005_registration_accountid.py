# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-02 18:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ys', '0004_remove_registration_accountid'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='AccountID',
            field=models.CharField(default='', max_length=128, unique=True),
        ),
    ]
