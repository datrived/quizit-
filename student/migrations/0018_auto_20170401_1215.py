# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-01 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0017_auto_20170401_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard_activity_log',
            name='timestamp',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='student_activity_log',
            name='timestamp',
            field=models.DateTimeField(blank=True),
        ),
    ]
