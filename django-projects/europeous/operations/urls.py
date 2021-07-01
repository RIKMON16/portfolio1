from django.urls import path

from operations import views

urlpatterns = [
    path('', views.ops, name='landing-ops'),
]