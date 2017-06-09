# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-08 18:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ccreator', '0019_remove_character_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
