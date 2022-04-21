from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('customer', views.customer, name='customer'),
    path('seller', views.seller, name='seller')
]