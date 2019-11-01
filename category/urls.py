from django.conf.urls import url
from category import views
urlpatterns = [
     url(r'^(?P<category>[A-Z]+)/$',views.mobile_phones,name="category"),
    url(r'^brand',views.brands,name="brand"),
    url(r'^state',views.state,name="state"),
    url(r'^accessory',views.accessory,name="accessory"),   
]