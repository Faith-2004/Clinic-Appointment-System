from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_appointment, name='book_appointment'),
    path('my/', views.my_appointments, name='my_appointments'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('update/<int:appointment_id>/<str:status>/', views.update_appointment, name='update_appointment'),
]