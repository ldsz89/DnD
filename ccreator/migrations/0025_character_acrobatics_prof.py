# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-23 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccreator', '0024_auto_20170613_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='acrobatics_prof',
            field=models.BooleanField(default=False),
        ),
    ]