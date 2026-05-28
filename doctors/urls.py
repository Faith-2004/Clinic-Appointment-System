from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctor_list, name='doctor_list'),
    path('add/', views.add_doctor, name='add_doctor'),
    path('edit/<int:doctor_id>/', views.edit_doctor, name='edit_doctor'),
    path('delete/<int:doctor_id>/', views.delete_doctor, name='delete_doctor'),
    path('browse/', views.browse_doctors, name='browse_doctors'),
]