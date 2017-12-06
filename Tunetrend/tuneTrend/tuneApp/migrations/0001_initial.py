# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArtistsProper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('artist_name', models.CharField(max_length=255, blank=True)),
                ('spotify_identifier', models.CharField(max_length=255, blank=True)),
                ('artist_id', models.CharField(max_length=255, blank=True)),
                ('artist_popularity', models.IntegerField(null=True, blank=True)),
                ('artist_followers', models.IntegerField(null=True, blank=True)),
                ('collection_time', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'artists_proper',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=80)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField()),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(unique=True, max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=75)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, serialize=False, primary_key=True)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SongsProper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('artist', models.CharField(max_length=255, blank=True)),
                ('artist_id', models.CharField(max_length=255, blank=True)),
                ('song_name', models.CharField(max_length=255, blank=True)),
                ('spotify_identifier', models.CharField(max_length=255, blank=True)),
                ('song_id', models.CharField(max_length=255, blank=True)),
                ('song_popularity', models.IntegerField(null=True, blank=True)),
                ('collection_time', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'songs_proper',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TwitterInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('artist', models.CharField(max_length=255, blank=True)),
                ('artist_id', models.CharField(max_length=255, blank=True)),
                ('song', models.CharField(max_length=255, blank=True)),
                ('song_id', models.CharField(max_length=255, blank=True)),
                ('artist_references', models.IntegerField(null=True, blank=True)),
                ('song_references', models.IntegerField(null=True, blank=True)),
                ('collected_on', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'twitter_info',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
