# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-20 14:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_sitebanner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compdetail',
            name='cd_description',
        ),
      
    ]
