# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-01 03:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0003_auto_20161019_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recordimg',
            name='record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imgs_set', to='record.Record'),
        ),
    ]
