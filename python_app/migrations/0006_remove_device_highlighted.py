# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 08:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('python_app', '0005_auto_20161115_1337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='highlighted',
        ),
    ]