# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-06 02:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('knowItAllAPI', '0006_auto_20171106_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taglinker',
            name='pollID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='knowItAllAPI.Poll'),
        ),
        migrations.AlterField(
            model_name='taglinker',
            name='topicID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='knowItAllAPI.Topic'),
        ),
    ]