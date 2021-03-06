# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-03 08:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_remove_tweet_content2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='content1',
        ),
        migrations.AddField(
            model_name='tweet',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tweet',
            name='updated',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2018, 3, 3, 8, 5, 24, 116626, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
