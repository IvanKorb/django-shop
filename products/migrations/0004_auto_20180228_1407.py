# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-28 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='author',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
