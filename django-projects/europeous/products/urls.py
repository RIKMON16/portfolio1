from django.urls import path

from products import views

urlpatterns = [
    path('addproducts/', views.prd, name='landing'),
    path('hotel/', views.hotel, name='addhotel'),
]
