# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-12-04 23:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='logistics',
            field=models.ManyToManyField(to='warehouse.Logistics'),
        ),
        migrations.AlterField(
            model_name='warehouseorders',
            name='logistics',
            field=models.ManyToManyField(to='warehouse.Logistics'),
        ),
    ]
