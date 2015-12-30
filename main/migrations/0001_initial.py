# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-29 20:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Approval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('approved', models.CharField(choices=[('n', 'no'), ('-', 'pending'), ('y', 'yes')], default='-', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='ApprovalPriority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Approver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('notes', models.CharField(max_length=200)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=200)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0)),
                ('time', models.DateTimeField()),
                ('business_purpose', models.CharField(max_length=200)),
                ('closed', models.BooleanField(default=False)),
                ('items', models.ManyToManyField(to='main.Item')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Requester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('notes', models.CharField(max_length=200)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VendorInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address_first', models.CharField(max_length=200)),
                ('address_second', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('st', models.CharField(max_length=200)),
                ('zip', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('fax', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WorkflowTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('approval_list', models.ManyToManyField(to='main.ApprovalPriority')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.PaymentMethod'),
        ),
        migrations.AddField(
            model_name='order',
            name='requester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Requester'),
        ),
        migrations.AddField(
            model_name='order',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.VendorInformation'),
        ),
        migrations.AddField(
            model_name='order',
            name='workflow_template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.WorkflowTemplate'),
        ),
        migrations.AddField(
            model_name='approvalpriority',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Approver'),
        ),
        migrations.AddField(
            model_name='approval',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Approver'),
        ),
    ]