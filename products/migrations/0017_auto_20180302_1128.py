# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-02 05:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20180228_1510'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='update',
            new_name='updated',
        ),
        migrations.RenameField(
            model_name='productimage',
            old_name='update',
            new_name='updated',
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='products_images/'),
        ),
    ]
