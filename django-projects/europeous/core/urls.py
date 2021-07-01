from django.urls import path

from core import views

urlpatterns = [
    path('home/', views.main, name='landing-page'),
]
