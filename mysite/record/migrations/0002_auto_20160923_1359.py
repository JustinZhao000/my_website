# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-23 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='article_description',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='\u6982\u89c8'),
        ),
    ]
