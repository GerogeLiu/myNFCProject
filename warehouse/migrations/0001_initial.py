# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-12-04 12:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customerID', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('customerName', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=1024)),
                ('phone', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=64)),
                ('createTime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productID', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('productName', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('storeID', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('storeName', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerAccount',
            fields=[
                ('customerID', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='NFCwarehouse.Customer')),
                ('customerUserName', models.CharField(default='customer', max_length=64)),
                ('customerPassword', models.CharField(default='666666', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('productID', models.OneToOneField(auto_created=True, default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='NFCwarehouse.Product')),
                ('color', models.CharField(max_length=32)),
                ('style', models.CharField(max_length=64)),
                ('size', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='store',
            name='customerID',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='store_owner', to='NFCwarehouse.Customer'),
        ),
        migrations.AddField(
            model_name='product',
            name='customerID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NFCwarehouse.Customer'),
        ),
        migrations.AddField(
            model_name='product',
            name='store',
            field=models.ManyToManyField(to='NFCwarehouse.Store'),
        ),
        migrations.AddField(
            model_name='customer',
            name='employeeID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_creator', to=settings.AUTH_USER_MODEL),
        ),
    ]
