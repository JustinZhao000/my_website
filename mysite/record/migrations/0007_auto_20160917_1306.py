# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-17 13:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0006_auto_20160917_1257'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='type',
            new_name='record_type',
        ),
        migrations.RemoveField(
            model_name='recordtype',
            name='record_type',
        ),
        migrations.AddField(
            model_name='recordtype',
            name='type_label',
            field=models.CharField(default=datetime.datetime(2016, 9, 17, 13, 5, 48, 369057, tzinfo=utc), max_length=10, verbose_name='\u7c7b\u578b\u5173\u952e\u5b57'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recordtype',
            name='type_name',
            field=models.CharField(default=datetime.datetime(2016, 9, 17, 13, 6, 3, 18496, tzinfo=utc), max_length=10, verbose_name='\u7c7b\u578b\u540d\u79f0'),
            preserve_default=False,
        ),
    ]
