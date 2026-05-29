from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('facilities/', views.facilities, name='facilities'),
    path('emergency/', views.emergency, name='emergency'),
    path('contact/', views.contact, name='contact'),
    path('medical-services/', views.medical_services, name='medical_services'),
]