# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-28 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20180228_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='genre_book',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='pages_count',
            field=models.IntegerField(blank=True, default=None, max_length=4, null=True),
        ),
    ]
