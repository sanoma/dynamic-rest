# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-17 06:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0004_user_is_dead'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.TextField(unique=True),
        ),
    ]