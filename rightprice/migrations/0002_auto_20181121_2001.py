# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-21 20:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rightprice', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carmodel',
            old_name='model_text',
            new_name='model_choice',
        ),
        migrations.RenameField(
            model_name='carmodel',
            old_name='model',
            new_name='name',
        ),
    ]
