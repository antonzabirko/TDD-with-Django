# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2019-12-26 04:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]