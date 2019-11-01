# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
# Create your models here.



class GeneralProduct(models.Model):
    CATEGORIES = (
        ('MOB','Mobile Phone'),
        ('COM','Computer'),
        ('MBA','Mobile Accessory'),
        ('CMA','Computer Accessory'),
        ('O','Other')
        )
    BRANDS = (
        ('SAM','Samsung'),
        ('APP','Apple'),
        ('TEC','Techno'),
        ('LG','LG'),
        ('SON','Sony'),
        ('NOK','Nokia'),
        ('YEZ','Yezz'),
        ('ITE','Itel'),
        ('BBR','BlackBerry'),
        ('HTC','HTC'),
        ('DEL','Dell'),
        ('TOS','Toshiba'),
        ('LEN','Lenovo'),
        ('HP','HP'),
        ('MOT','Motorola'),
        ('HUA','Huawei'),
        ('ASU','Asus'),
        ('GOO','Google'),
        ('ACE','Acer'),
        ('BLU','Blu'),
        ('ALC','Alcatel'),
        ('PAN','Panasonic'),
        ('VIV','Vivo'),
        ('OPP','Oppo'),
        ('HON','Honor'),
        ('ONP','OnePlus'),
        ('QKU','QIKU'),
        ('SMT','Smartisan'),
        ('XIA','Xiaomi'),
        ('MEI','Meizu'),
        ('O','Other')
        )
    STATE = (
    ('NW','New'),
    ('UD','Used')
    )

    gp_category = models.CharField("Category",max_length=3,choices=CATEGORIES,default='MOB')
    gp_brand = models.CharField("brand",max_length=3,choices=BRANDS,default='SAM',blank=True,null=True)
    gp_name = models.CharField("name",max_length=50,blank=False)
    gp_dateAdded = models.DateField("date Added",auto_now=True)
    gp_quantity = models.IntegerField("quantity",blank=True)
    gp_available = models.BooleanField("available")
    gp_state = models.CharField("state",max_length=2, choices=STATE, default='NW')
    gp_price = models.DecimalField("price", max_digits=9, decimal_places=2,blank=False)
    gp_main_img = models.ImageField("Main Image",blank=True, null=True,upload_to="images/%m/")
    gp_img2 = models.ImageField("image2",blank=True, null=True,upload_to="images/%m/")
    gp_img3 = models.ImageField("image3",blank=True, null=True,upload_to="images/%m/")
    gp_img4 = models.ImageField("image4",blank=True, null=True,upload_to="images/%m/")
    gp_description = models.CharField("Product Description",max_length=200,blank=True,null=True)
    
    class Meta:
        ordering = ['gp_dateAdded']
        verbose_name = 'Product'
        
    def __str__(self):
        return self.gp_name
    
    def get_absolute_url(self):
        return reverse('store:itemInfo',args=[self.id])

   
class UsedProduct(models.Model):
    used_product = models.ForeignKey(GeneralProduct,on_delete=models.CASCADE, null=True, limit_choices_to={"gp_state":"UD"})
    used_duration = models.IntegerField("used Duration")#used duration in months
    used_description = models.CharField("usage Description",max_length=200)
       
    def __str__(self):
        return self.used_product.gp_name
    class Meta:
        verbose_name ='Used Detail'
        ordering = ['used_duration']
        
class CompDetail(models.Model):
    COMP_TYPES = (('D','Desktop'),
            ('L','Laptop')
            )
    cd_product = models.ForeignKey(GeneralProduct,on_delete=models.CASCADE,limit_choices_to={"gp_category":"COM"})
    cd_type = models.CharField("type of Computer",max_length=1,choices=COMP_TYPES,blank=True)
    cd_os = models.CharField("OS",max_length=60,blank=True)
    cd_cpu = models.CharField("CPU size",max_length=60,blank=True)
    cd_gpu = models.CharField("GPU info",max_length=60,blank=True)
    cd_gpu_num = models.IntegerField("GPU size number", blank=True)#gpu in number
    cd_size = models.CharField("size of item",max_length=60,blank=True)
    cd_size_num = models.IntegerField("size")
    cd_ram = models.CharField("RAM info",max_length=60,blank=True)
    cd_ram_num = models.IntegerField("RAM size number")
    cd_storage = models.CharField("storage size",max_length=60,blank=True)
    cd_storage_num = models.IntegerField("storage size number")
   
    def fieldValues(self):
      myList = [self.cd_type,self.cd_os,self.cd_cpu,self.cd_gpu,
               self.cd_size,self.cd_ram,self.cd_storage]
      return myList
    
    class Meta:
        ordering = ['cd_os']
        verbose_name = "Computer Detail"
    def __str__(self):
        return self.cd_product.gp_name
    
class MobiDetail(models.Model):
    gen = GeneralProduct()
    SIM_TYPE = (
        ('S','Single Sim'),
        ('D','Dual Sim')
    )
    MOBILE_TYPES = (
        ('SM','Smart Phone'),
        ('SP','Simple Phone'),
        ('TA','Tablet')
    )
  
    m_product = models.ForeignKey(GeneralProduct,on_delete=models.CASCADE,limit_choices_to={"gp_category":"MOB"})
    m_type = models.CharField("type of mobile device",max_length=2, choices=MOBILE_TYPES, default= 'SM')
    m_os = models.CharField("OS",max_length=60)
    m_cpu = models.CharField("CPU size",max_length=60)
    m_size = models.CharField("size of item",max_length=60)
    #below only used for categorizing not to display
    m_size_num = models.DecimalField("size",max_digits=3, decimal_places=1)
    m_int_memory = models.CharField("internal memory",max_length=60)
    m_storage = models.CharField("storage size",max_length=60)
    #below only used for categorizing not to display
    m_storage_num = models.IntegerField("Storage Size")
    m_has_wifi = models.BooleanField("Wifi Capable", default=True)
    m_has_bluetooth = models.BooleanField("bluetooth Capable", default=True)
    m_has_gps = models.BooleanField("GPS Capable", default=True)
    m_simcard = models.CharField("sim type",max_length=1,choices=SIM_TYPE,default='S')
    m_camera_px = models.IntegerField("camera pixels")
 
    
    def __str__(self):
        return self.m_product.gp_name
    
    def fieldValues(self):
        myList = [self.m_type,self.m_os,self.m_cpu,self.m_size,self.m_int_memory,self.m_storage,self.m_has_wifi,self.m_has_bluetooth,self.m_has_gps,self.m_simcard,self.m_camera_px]
        
        return myList
    class Meta:
        verbose_name ='Mobile Detail'
        ordering = ['m_type']
   
 
class MemoryUpgrade(models.Model):
    #This class is for uploading memory for different devices
    MEMORY_ITEM = (
    ('FLD','Flash Drive'),
    ('HDD','Hard Drive'),
    ('SSD','Solid State Drive'),
    ('RAM','RAM'),
    ('MSD','Memory Card')
    )
    
    DEVICE_TYPE = (
        ('PC','Computer'),
        ('MOB','Mobile/Other')
    )
    
    RAM_TYPE = (
        ('PC1','PC1'),
        ('PC2','PC2'),
        ('PC3','PC3'))
    
    mem_product = models.ForeignKey(GeneralProduct,on_delete=models.CASCADE,blank=True, null=True, limit_choices_to={'gp_category':'MBA','gp_category':'CMA'})
    mem_type = models.CharField("memory Type",max_length=3,choices=MEMORY_ITEM)
    mem_for = models.CharField("memory for",max_length=3,choices=DEVICE_TYPE)
    mem_size = models.IntegerField("size")
    
    def __str__(self):
        return self.mem_type
    class Meta:
        verbose_name ='Memory Upgrade'
    
    def fieldValues(self):
        myList = [self.mem_type,self.mem_for,self.mem_size]
        return myList
        
        
class CompAccessory(models.Model):
    ACCESSORY = (
     ('SPK','Speaker'),
     ('FLD','Flashdrive'),
     ('HDD','Hard Drive'),
     ('KYB','Keyboard'),
     ('MTR','Monitor'),
     ('MEM','Memory'),
     ('LTC','Laptop Charger'),
     ('RTR','Networking'),
     ('DDT','Digital Drawing Tablet'),
     ('STU','System Unit'),
     ('ACA','AC adapter'),
     ('LB','Laptop Bag'),
     ('DTC','Data Cable'),
     ('HST','Headset'),
     ('SPK','Speaker'),
     ('O','Other')
    )
    
    ca_product = models.ForeignKey(GeneralProduct,on_delete=models.CASCADE,blank=True, null=True, limit_choices_to={'gp_category':'CMA'})
    ca_memory = models.ForeignKey(MemoryUpgrade,on_delete=models.CASCADE,blank=True, null=True, limit_choices_to={'mem_for':'PC'})
    ca_accessory_type = models.CharField(max_length=3,blank=False,choices=ACCESSORY)
    
    def __str__(self):
        return self.ca_accessory_type
    class Meta:
        verbose_name ='Computer Accessory'
        verbose_name_plural = 'Computer Accessories'
    def fieldValues(self):
        return [self.ca_accessory_type]
class MobiAccessory(models.Model):
    ACCESSORY = (
     ('EPC','Ear Piece'),
     ('CK','Car Kit'),
     ('RPT','Repair Tools'),
     ('SCR','Replacement Screen'),
     ('MEM','Memory'),
     ('BAT','Battery'),
     ('PHC','Phone Case'),
     ('PTC','Protective Screen'),
     ('CHA','Charger'),
     ('HF','Hands Free'),
     ('O','Other')
    )
    ma_product = models.ForeignKey(GeneralProduct,on_delete=models.CASCADE,blank=True, null=True, limit_choices_to={'gp_category':'MBA'})
    ma_memory = models.ForeignKey(MemoryUpgrade,on_delete=models.CASCADE,blank=True,null=True,limit_choices_to={'mem_for':'MOB'})
    ma_accessory_type = models.CharField("accessory",max_length=3,choices=ACCESSORY,blank=False)
    
    def __str__(self):
        return self.ma_accessory_type
   
    class Meta:
        verbose_name ='Mobile Accessory'
        verbose_name_plural = 'Mobile Accessories'
    def fieldValues(self):
        myList = [self.ma_accessory_type]
        return myList
        
class siteBanner(models.Model):
    name = models.CharField(max_length=100, blank=True,null=True)
    image = models.ImageField(upload_to="images/%m/", null=True)
    public = models.BooleanField('make public')
    uploaded_at = models.DateField(auto_now=True)
    description = models.CharField(max_length=255, null=True, blank=False)
    
    class Meta:
        verbose_name = 'Site Banner'
    def __str__(self):
        return self.name
    

  