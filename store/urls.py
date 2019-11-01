from django.conf.urls import url
from store import views


urlpatterns = [
    url(r'^/',views.Main,name="home"), 
    url(r'^products/(?P<page_id>\d+)/$',views.new_product_list,name="newProducts"),
    url(r'^item_info/(?P<item_id>\d+)/$',views.item_info, name="itemInfo"),
    url(r'^about',views.about, name="about"),
       
]