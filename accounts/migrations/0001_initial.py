# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-20 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('text', models.TextField()),
                ('gender', models.CharField(choices=[(b'M', b'Male'), (b'F', b'Female')], default=b'M', max_length=6)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
