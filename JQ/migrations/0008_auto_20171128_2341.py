# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-29 04:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JQ', '0007_auto_20171118_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='size',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
