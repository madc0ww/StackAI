# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-05 07:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1024)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('score', models.IntegerField()),
                ('text', models.TextField()),
                ('creationDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('postTypeId', models.IntegerField(choices=[(1, b'Question'), (2, b'Answer')])),
                ('creationDate', models.DateTimeField()),
                ('score', models.IntegerField()),
                ('viewCount', models.IntegerField()),
                ('body', models.TextField()),
                ('lastEditorDisplayName', models.CharField(max_length=200)),
                ('lastEditDate', models.DateTimeField()),
                ('lastActivityDate', models.DateTimeField()),
                ('communityOwnedDate', models.DateTimeField()),
                ('title', models.CharField(max_length=1024)),
                ('tags', models.TextField()),
                ('answerCount', models.IntegerField()),
                ('commentCount', models.IntegerField()),
                ('favoriteCount', models.IntegerField()),
                ('closedDate', models.DateTimeField()),
                ('acceptedAnswerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_answer', to='dataHandler.Post')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('reputation', models.IntegerField()),
                ('creationDate', models.DateTimeField()),
                ('displayName', models.CharField(max_length=200)),
                ('lastAccessDate', models.DateTimeField()),
                ('webSiteURL', models.URLField()),
                ('location', models.CharField(max_length=1024)),
                ('age', models.IntegerField()),
                ('aboutMe', models.TextField()),
                ('upVotes', models.IntegerField()),
                ('downVotes', models.IntegerField()),
                ('emailHash', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('voteTypeId', models.IntegerField(choices=[(1, b'AcceptedByOriginator'), (2, b'UpMod'), (3, b'DownMod'), (4, b'Offensive'), (5, b'Favorite'), (6, b'Close'), (7, b'Reopen'), (8, b'BountyStart'), (9, b'BountyClose'), (10, b'Deletion'), (11, b'Undeletion'), (12, b'Spam'), (13, b'InfoModerator')])),
                ('creationDate', models.DateTimeField()),
                ('BountyAmount', models.IntegerField()),
                ('postId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataHandler.Post')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataHandler.User')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='lastEditorUserId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='last_editor', to='dataHandler.User'),
        ),
        migrations.AddField(
            model_name='post',
            name='ownerUserId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_owner', to='dataHandler.User'),
        ),
        migrations.AddField(
            model_name='post',
            name='postId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='base_question', to='dataHandler.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='postId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataHandler.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataHandler.User'),
        ),
        migrations.AddField(
            model_name='badge',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataHandler.User'),
        ),
    ]
