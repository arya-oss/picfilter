# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 19:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import iauth.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=11)),
                ('birthdate', models.DateField(null=True)),
                ('gender', models.CharField(max_length=1)),
                ('picture', models.ImageField(blank=True, upload_to=iauth.models.upload_profile)),
                ('ipAddress', models.CharField(blank=True, max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
