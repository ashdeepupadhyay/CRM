from django.urls import path
from . import views

app_name='accounts'

urlpatterns = [
    path('',views.home,name='home' ),
    path('customer/<str:pk_test>',views.customer,name='customer'),
    path('products/',views.products,name='products'),
    
]
