# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 04:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('python_app', '0003_device_user_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Testimony',
            new_name='Reading',
        ),
        migrations.RenameField(
            model_name='reading',
            old_name='testimony_id',
            new_name='reading_id',
        ),
    ]