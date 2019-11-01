# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from store.models import GeneralProduct
from django.core.paginator import Paginator

# Create your views here.
def product_search_list(request):
    query = ""
    if request.method == 'GET': 
        #to check whether get reuest is made
        query = request.GET.get('k')
        #the request.GET.get() method is used to 
        #retrive submiitted data in key value format
        
        print(query)
    p = GeneralProduct
    products = p.objects.filter(gp_name__icontains= query)
    #__icontains used to query items with case insensitivity
    
   
    
    paginator = Paginator(products,1)
    myPage = request.GET.get('page')
    productPages = paginator.page(myPage)
    
    context = {
        'paginate':paginator,
        'object_list': productPages,
        'search_query':query
    }
    return render(request,'search/search_page.html',context)