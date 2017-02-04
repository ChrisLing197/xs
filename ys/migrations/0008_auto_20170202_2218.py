# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-02 22:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ys', '0007_auto_20170202_1931'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Transaction_id', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='registration',
            name='email',
        ),
        migrations.AddField(
            model_name='transactiontable',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listings', to='ys.Registration'),
        ),
    ]
