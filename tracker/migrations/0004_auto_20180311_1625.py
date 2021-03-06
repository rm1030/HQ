# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-11 20:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20180311_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='count_complete',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='count_tasks',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='percent_complete',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='percent_overdue',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
