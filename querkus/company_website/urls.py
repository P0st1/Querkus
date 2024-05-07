from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('o-nas', views.about_us, name='about_us')
]
