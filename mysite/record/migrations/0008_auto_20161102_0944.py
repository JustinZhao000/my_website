# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-02 01:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0007_remove_contactdata_qq_wechat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactdata',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u59d3\u540d'),
        ),
        migrations.AlterField(
            model_name='contactdata',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u7535\u8bdd'),
        ),
    ]
