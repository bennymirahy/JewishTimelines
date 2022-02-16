# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2022-02-16 20:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_todo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1024)),
                ('source', models.CharField(max_length=512)),
                ('age', models.IntegerField()),
                ('sourceAge', models.CharField(max_length=512)),
            ],
        ),
    ]