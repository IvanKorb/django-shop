# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-28 09:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20180228_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pages_count',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]