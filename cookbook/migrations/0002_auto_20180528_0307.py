# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-28 03:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['page_number']},
        ),
        migrations.AddField(
            model_name='page',
            name='manual',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='page',
            name='ocr',
            field=models.BooleanField(default=False),
        ),
    ]
