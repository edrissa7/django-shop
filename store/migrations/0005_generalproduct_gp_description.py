# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-06-26 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20190120_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalproduct',
            name='gp_description',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Product Description'),
        ),
    ]