# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 02:15
from __future__ import unicode_literals

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowItAllAPI', '0004_alltags_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='anonymous',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='review',
            name='anonymous',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='topic',
            name='anonymous',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='alltags',
            name='type',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(default='', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='text',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='notification',
            name='type',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='poll',
            name='text',
            field=models.CharField(default='', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='pollchoice',
            name='text',
            field=models.CharField(default='', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='topic',
            name='title',
            field=models.CharField(default='', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]