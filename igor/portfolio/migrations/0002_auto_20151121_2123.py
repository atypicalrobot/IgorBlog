# -*- coding: utf-8 -*-
# Generated by Django 1.9c1 on 2015-11-21 21:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publications',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='publications',
            name='abstract',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publications',
            name='published_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
