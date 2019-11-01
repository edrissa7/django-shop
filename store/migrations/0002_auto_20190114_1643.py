# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-14 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        
        migrations.AlterField(
            model_name='generalproduct',
            name='gp_img2',
            field=models.ImageField(blank=True, null=True, upload_to='images/%m/', verbose_name='image2'),
        ),
        migrations.AlterField(
            model_name='generalproduct',
            name='gp_img3',
            field=models.ImageField(blank=True, null=True, upload_to='images/%m/', verbose_name='image3'),
        ),
        migrations.AlterField(
            model_name='generalproduct',
            name='gp_img4',
            field=models.ImageField(blank=True, null=True, upload_to='images/%m/', verbose_name='image4'),
        ),
        migrations.AlterField(
            model_name='generalproduct',
            name='gp_main_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/%m/', verbose_name='Main Image'),
        ),
    ]
