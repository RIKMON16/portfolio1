from django.urls import path

from sales import views

urlpatterns = [
    path('', views.sal, name='sal'),
]
