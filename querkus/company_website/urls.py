from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('o-nas/', views.about_us, name='about_us'),
    path('kontakt/', views.contact, name='contact'),
    path('storitve/', views.services, name='services'),
    path('storitve/<str:title>/', views.service_detail, name='service_detail'),
]
