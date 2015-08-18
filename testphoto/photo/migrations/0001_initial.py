# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('src', models.CharField(max_length=50)),
                ('user_id', models.PositiveIntegerField()),
                ('created', models.DateTimeField()),
                ('likes', models.PositiveIntegerField()),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='Tagstate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.PositiveSmallIntegerField(default=0, choices=[(0, b'Published'), (1, b'Hidden')])),
                ('tag', models.ForeignKey(to='taggit.Tag')),
            ],
        ),
    ]
