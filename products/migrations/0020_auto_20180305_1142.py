# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-05 05:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20180305_1141'),
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
    ]