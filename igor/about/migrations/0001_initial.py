# -*- coding: utf-8 -*-
# Generated by Django 1.9c1 on 2015-11-21 15:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=255)),
                ('body', models.CharField(max_length=255)),
                ('icon', models.CharField(max_length=50)),
            ],
        ),
    ]
