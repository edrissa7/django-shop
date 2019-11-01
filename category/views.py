# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.paginator import Paginator
from store.models import (GeneralProduct,MobiAccessory,CompAccessory)
# Create your views here.
#method below for categories
def mobile_phones(request,category):
    obj = GeneralProduct
    item_list = obj.objects.filter(gp_category=category)
    
    paginator = Paginator(item_list,1)
    page = request.GET.get('page',1)
    productsPages = paginator.page(page)

    context = {
      'object':productsPages,
      'products':paginator
  }
    return render(request,'category/category.html',context)

def brands(request):
    obj = GeneralProduct
    item_list = obj.objects.filter(gp_brand="SAM")
    return render(request,'category/brand.html',{'object':item_list})

def state(request):
    obj = GeneralProduct
    item_list = obj.objects.filter(gp_state="NW")
    return render(request,'category/state.html',{'object':item_list})

def accessory(request):
  obj = MobiAccessory
  item_list = obj.objects.all()
    
  paginator = Paginator(item_list,1)
  page = request.GET.get('page',1)
  productsPages = paginator.page(page)

  context = {
      'object':productsPages,
      'products':paginator
  }
  return render(request,'category/accessory.html',context)

def comp_accessory(request):
  obj = CompAccessory
  item_list = obj.objects.all()
  return render(request,'category/comp_accessory.html',{'object':item_list})

