from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('patients/', views.patient_list, name='patient_list'),
    path('delete-patient/<int:user_id>/', views.delete_patient, name='delete_patient')
]