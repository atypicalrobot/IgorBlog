# -*- coding: utf-8 -*-
# Generated by Django 1.9c1 on 2015-11-21 20:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_about'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name_plural': 'About'},
        ),
        migrations.AddField(
            model_name='about',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='about/'),
        ),
    ]
