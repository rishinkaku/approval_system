# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-30 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='approvals',
            field=models.ManyToManyField(to='main.Approval'),
        ),
    ]
