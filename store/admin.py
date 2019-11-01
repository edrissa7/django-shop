# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *
# Register your models here.

class GeneralProductAdmin(admin.ModelAdmin):
    list_display = ['gp_name','gp_dateAdded','gp_quantity','gp_available','gp_price','gp_state','gp_category','gp_brand','gp_description','gp_main_img','gp_img2','gp_img3','gp_img4']
    list_filter = ['gp_dateAdded','gp_quantity','gp_available','gp_price','gp_state','gp_brand']
    list_editable = ['gp_quantity','gp_available','gp_price','gp_state','gp_category','gp_brand','gp_description','gp_main_img','gp_img2','gp_img3','gp_img4']
admin.site.register(GeneralProduct,GeneralProductAdmin)


class UsedProductAdmin(admin.ModelAdmin):
    list_display = ['used_product','used_duration','used_description']
    list_filter = ['used_duration']
    list_editable = ['used_duration','used_description']
admin.site.register(UsedProduct,UsedProductAdmin)

class CompDetailAdmin(admin.ModelAdmin):
    list_display = ['cd_product','cd_type','cd_os','cd_cpu','cd_gpu','cd_gpu_num','cd_size','cd_size_num','cd_ram','cd_ram_num','cd_storage','cd_storage_num']
    
    list_filter = ['cd_size_num','cd_type','cd_gpu_num','cd_ram_num','cd_storage_num']
    list_editable = ['cd_type','cd_os','cd_cpu','cd_gpu','cd_gpu_num','cd_size','cd_size_num','cd_ram','cd_ram_num','cd_storage','cd_storage_num']
    
admin.site.register(CompDetail,CompDetailAdmin)


class MobiDetailAdmin(admin.ModelAdmin):
     list_display = ['m_product','m_os','m_cpu','m_size','m_size_num','m_int_memory','m_has_wifi',
                     'm_has_bluetooth','m_has_gps','m_simcard','m_storage','m_storage_num','m_camera_px']
     list_filter = ['m_size_num','m_storage_num','m_has_wifi','m_has_bluetooth','m_has_gps','m_simcard']
     list_editable = ['m_os','m_cpu','m_size','m_size_num','m_int_memory','m_has_wifi',
                     'm_has_bluetooth','m_has_gps','m_simcard','m_storage','m_storage_num','m_camera_px']
admin.site.register(MobiDetail,MobiDetailAdmin)

class MemoryUpgradeAdmin(admin.ModelAdmin):
    list_display = ['mem_product','mem_type','mem_for','mem_size']
    list_filter = ['mem_type','mem_for','mem_size']
    list_editable = ['mem_type','mem_for','mem_size']
admin.site.register(MemoryUpgrade,MemoryUpgradeAdmin)

class MobiAccessoryAdmin(admin.ModelAdmin):
    list_display = ['ma_product','ma_memory','ma_accessory_type']
    list_filter = ['ma_memory','ma_accessory_type']
    list_editable = ['ma_memory','ma_accessory_type']
admin.site.register(MobiAccessory,MobiAccessoryAdmin) 

class CompAccessoryAdmin(admin.ModelAdmin):
    list_display = ['ca_product','ca_memory','ca_accessory_type']
    list_filter = ['ca_memory','ca_accessory_type']
    list_editable = ['ca_memory','ca_accessory_type']
admin.site.register(CompAccessory,CompAccessoryAdmin)

class siteBannerAdmin(admin.ModelAdmin):
    list_display = ['name','image','public','uploaded_at','description']
    list_filter = ['public','uploaded_at']
    list_editable = ['image','public','description']
admin.site.register(siteBanner,siteBannerAdmin)


