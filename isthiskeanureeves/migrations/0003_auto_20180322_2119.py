# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-22 21:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isthiskeanureeves', '0002_auto_20180322_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]