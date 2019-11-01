from django.conf.urls import url
from search import views

urlpatterns = [
    url(r'^',views.product_search_list, name="product_search")
]