# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 00:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('knowItAllAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='text',
            field=models.CharField(default=b'', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='pollchoice',
            name='text',
            field=models.CharField(default=b'', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='topicID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='knowItAllAPI.Topic', unique=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(default=b'', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='vote',
            name='pollChoiceID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='knowItAllAPI.PollChoice', unique=True),
        ),
    ]
