# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-08 18:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ccreator', '0016_character_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='user',
        ),
    ]
