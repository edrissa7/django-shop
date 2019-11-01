# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse
#from django.urls import reverse
from django.http import HttpResponse,Http404
from .models import(GeneralProduct,UsedProduct,CompDetail,MemoryUpgrade,
                    CompAccessory,siteBanner,MobiAccessory,
                    MobiDetail)
from django.core.paginator import Paginator

# Create your views here.
def Main(request):
    num = 'Hello'
    #setting objects for dislaying banner images
    site_banner = siteBanner
    image_obj = site_banner.objects.filter(public=True)
    
    
    
    #loading products that are available from the GP model        
    p = GeneralProduct
    products = p.objects.all()
    
    
    #using pagination
    paginator = Paginator(products,4)
    page = request.GET.get('page',1)
    productPages = paginator.page(page)
    
    #trying a crete a paginator list that eliminates 1
    page_count = []
    for x in paginator.page_range:
        if x != 1:      
          page_count.append(x)
        
    context = {
        'value':num,
        'products':productPages,
        'paginator':paginator,
        'img_obj':image_obj,
        'paginate':page_count
    }
    #render page
    return render(request,'base.html',context)

#product list page
def new_product_list(request,page_id):
    
    p = GeneralProduct
    products = p.objects.all()
    
    paginator = Paginator(products,2)   
    productPages = paginator.page(page_id)
    
    page_count = []
    for x in paginator.page_range:
        if x != 1:      
          page_count.append(x)
        
    context = {
        'paginator': paginator,
         'object':productPages,
        'paginate':page_count
    }
    return render(request,'products.html',context)
    

#request and request parameter
def item_info(request,item_id):
    
    md = MobiDetail #Mobidetail instance
    cd = CompDetail
    ma = MobiAccessory
    ca = CompAccessory
    mu = MemoryUpgrade
    gen = GeneralProduct
    
    specific_details = []
    basic_details = gen.objects.get(id=item_id)
    try: 
      if basic_details.gp_category=="MOB":
       specific_details = md.objects.get(m_product_id=item_id).fieldValues()
      elif basic_details.gp_category=="COM":
       specific_details = cd.objects.get(cd_product_id=item_id).fieldValues()
      elif basic_details.gp_category=="MBA":
       specific_details = ma.objects.get(ma_product_id=item_id).fieldValues()
      elif basic_details.gp_category=="CMA":
       specific_details = ca.objects.get(ca_product_id=item_id).fieldValues()
      
    except MobiDetail.DoesNotExist:
        specific_details = []
    except CompDetail.DoesNotExist:
        specific_details = []
    except MobiAccessory.DoesNotExist:
        specific_details = []
    except CompAccessory.DoesNotExist:
        specific_details = []
     

    return render(request,'item_info.html',{'items':basic_details,'more_items':specific_details})

def about(request):
    return render(request,'about.html')