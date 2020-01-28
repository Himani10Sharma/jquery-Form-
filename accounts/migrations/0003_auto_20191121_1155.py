# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-21 11:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191121_0553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='qualification',
        ),
        migrations.AddField(
            model_name='post',
            name='email',
            field=models.CharField(default=django.utils.timezone.now, max_length=70),
            preserve_default=False,
        ),
    ]