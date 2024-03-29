# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-26 15:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import datetime


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompAccessory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ca_accessory_type', models.CharField(choices=[('SPK', 'Speaker'), ('FLD', 'Flashdrive'), ('HDD', 'Hard Drive'), ('KYB', 'Keyboard'), ('MTR', 'Monitor'), ('MEM', 'Memory'), ('LTC', 'Laptop Charger'), ('RTR', 'Networking'), ('DDT', 'Digital Drawing Tablet'), ('STU', 'System Unit'), ('ACA', 'AC adapter'), ('LB', 'Laptop Bag'), ('DTC', 'Data Cable'), ('HST', 'Headset'), ('SPK', 'Speaker'), ('O', 'Other')], max_length=3)),
            ],
            options={
                'verbose_name': 'Computer Accessory',
                'verbose_name_plural': 'Computer Accessories',
            },
        ),
        migrations.CreateModel(
            name='CompDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cd_type', models.CharField(blank=True, choices=[('D', 'Desktop'), ('L', 'Laptop')], max_length=1, verbose_name='type of Computer')),
                ('cd_os', models.CharField(blank=True, max_length=60, verbose_name='OS')),
                ('cd_cpu', models.CharField(blank=True, max_length=60, verbose_name='CPU size')),
                ('cd_gpu', models.CharField(blank=True, max_length=60, verbose_name='GPU info')),
                ('cd_gpu_num', models.IntegerField(blank=True, verbose_name='GPU size number')),
                ('cd_size', models.CharField(blank=True, max_length=60, verbose_name='size of item')),
                ('cd_size_num', models.IntegerField(verbose_name='size')),
                ('cd_ram', models.CharField(blank=True, max_length=60, verbose_name='RAM info')),
                ('cd_ram_num', models.IntegerField(verbose_name='RAM size number')),
                ('cd_storage', models.CharField(blank=True, max_length=60, verbose_name='storage size')),
                ('cd_storage_num', models.IntegerField(verbose_name='storage size number')),
                ('cd_description', models.CharField(blank=True, max_length=200, verbose_name='description')),
            ],
            options={
                'ordering': ['cd_os'],
                'verbose_name': 'Computer Detail',
            },
        ),
        migrations.CreateModel(
            name='GeneralProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gp_category', models.CharField(choices=[('MOB', 'Mobile Phone'), ('COM', 'Computer'), ('MBA', 'Mobile Accessory'), ('CMA', 'Computer Accessory'), ('O', 'Other')], default='MOB', max_length=3, verbose_name='Category')),
                ('gp_brand', models.CharField(blank=True, choices=[('SAM', 'Samsung'), ('APP', 'Apple'), ('TEC', 'Techno'), ('LG', 'LG'), ('SON', 'Sony'), ('NOK', 'Nokia'), ('YEZ', 'Yezz'), ('ITE', 'Itel'), ('BBR', 'BlackBerry'), ('HTC', 'HTC'), ('DEL', 'Dell'), ('TOS', 'Toshiba'), ('LEN', 'Lenovo'), ('HP', 'HP'), ('MOT', 'Motorola'), ('HUA', 'Huawei'), ('ASU', 'Asus'), ('GOO', 'Google'), ('ACE', 'Acer'), ('BLU', 'Blu'), ('ALC', 'Alcatel'), ('PAN', 'Panasonic'), ('VIV', 'Vivo'), ('OPP', 'Oppo'), ('HON', 'Honor'), ('ONP', 'OnePlus'), ('QKU', 'QIKU'), ('SMT', 'Smartisan'), ('XIA', 'Xiaomi'), ('MEI', 'Meizu'), ('O', 'Other')], default='SAM', max_length=3, null=True, verbose_name='brand')),
                ('gp_name', models.CharField(max_length=50, verbose_name='name')),
                ('gp_dateAdded', models.DateField(auto_now=True, verbose_name='date Added')),
                ('gp_quantity', models.IntegerField(blank=True, verbose_name='quantity')),
                ('gp_available', models.BooleanField(verbose_name='available')),
                ('gp_state', models.CharField(choices=[('NW', 'New'), ('UD', 'Used')], default='NW', max_length=2, verbose_name='state')),
                ('gp_price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='price')),
                ('gp_main_img', models.ImageField(blank=True, null=True, upload_to='images/%m/')),
                ('gp_img2', models.ImageField(blank=True, null=True, upload_to='images/%m/')),
                ('gp_img3', models.ImageField(blank=True, null=True, upload_to='images/%m/')),
                ('gp_img4', models.ImageField(blank=True, null=True, upload_to='images/%m/')),
            ],
            options={
                'ordering': ['gp_dateAdded'],
                'verbose_name': 'Product',
            },
        ),
        migrations.CreateModel(
            name='MemoryUpgrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mem_type', models.CharField(choices=[('FLD', 'Flash Drive'), ('HDD', 'Hard Drive'), ('SSD', 'Solid State Drive'), ('RAM', 'RAM'), ('MSD', 'Memory Card')], max_length=3, verbose_name='memory Type')),
                ('mem_for', models.CharField(choices=[('PC', 'Computer'), ('MOB', 'Mobile/Other')], max_length=3, verbose_name='memory for')),
                ('mem_size', models.IntegerField(verbose_name='size')),
                ('mem_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.GeneralProduct')),
            ],
            options={
                'verbose_name': 'Memory Upgrade',
            },
        ),
        migrations.CreateModel(
            name='MobiAccessory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ma_accessory_type', models.CharField(choices=[('EPC', 'Ear Piece'), ('CK', 'Car Kit'), ('RPT', 'Repair Tools'), ('SCR', 'Replacement Screen'), ('MEM', 'Memory'), ('BAT', 'Battery'), ('PHC', 'Phone Case'), ('PTC', 'Protective Screen'), ('CHA', 'Charger'), ('HF', 'Hands Free'), ('O', 'Other')], max_length=3, verbose_name='accessory')),
                ('ma_memory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.MemoryUpgrade')),
                ('ma_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.GeneralProduct')),
            ],
            options={
                'verbose_name': 'Mobile Accessory',
                'verbose_name_plural': 'Mobile Accessories',
            },
        ),
        migrations.CreateModel(
            name='UsedProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('used_duration', models.IntegerField(verbose_name='used Duration')),
                ('used_description', models.CharField(max_length=200, verbose_name='usage Description')),
                ('used_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.GeneralProduct')),
            ],
            options={
                'ordering': ['used_duration'],
                'verbose_name': 'Used Detail',
            },
        ),
        migrations.AddField(
            model_name='compdetail',
            name='cd_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.GeneralProduct'),
        ),
        migrations.AddField(
            model_name='compaccessory',
            name='ca_memory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.MemoryUpgrade'),
        ),
        migrations.AddField(
            model_name='compaccessory',
            name='ca_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.GeneralProduct'),
        ),
    ]
