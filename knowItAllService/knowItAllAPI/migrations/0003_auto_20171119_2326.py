# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-19 23:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('knowItAllAPI', '0002_auto_20171117_2127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default=b'', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default=b'', max_length=200)),
                ('upvote', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='poll',
            name='opinionTotal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='review',
            name='opinionTotal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='opinion',
            name='pollID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='knowItAllAPI.Poll'),
        ),
        migrations.AddField(
            model_name='opinion',
            name='reviewID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='knowItAllAPI.Review'),
        ),
        migrations.AddField(
            model_name='opinion',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='pollID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='knowItAllAPI.Poll'),
        ),
        migrations.AddField(
            model_name='comment',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
