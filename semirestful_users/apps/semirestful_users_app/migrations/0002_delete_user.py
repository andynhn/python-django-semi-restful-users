# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-15 17:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('semirestful_users_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]