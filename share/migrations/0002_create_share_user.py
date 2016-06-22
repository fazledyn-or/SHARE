# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 00:27
from __future__ import unicode_literals

from django.db import migrations

def create_share_harvester_user(apps, schema_editor):
    ShareUser = apps.get_model('share', 'ShareUser')
    share_user = ShareUser.objects.create_harvester_user(username='share_oauth2_application_user', harvester='')


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_share_harvester_user),
    ]