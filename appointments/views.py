from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Appointment
from doctors.models import Doctor
from .emails import send_appointment_email


@login_required
def book_appointment(request):
    doctors = Doctor.objects.filter(available=True)

    if request.method == 'POST':
        doctor_id = request.POST['doctor']
        date = request.POST['date']
        time = request.POST['time']
        reason = request.POST['reason']

        doctor = Doctor.objects.get(id=doctor_id)

        Appointment.objects.create(
            patient=request.user,
            doctor=doctor,
            appointment_date=date,
            appointment_time=time,
            reason=reason,
            status='pending'
        )
        messages.success(request, 'Appointment booked! Waiting for approval.')
        return redirect('my_appointments')

    return render(request, 'appointments/book.html', {'doctors': doctors})


@login_required
def my_appointments(request):
    appointments = Appointment.objects.filter(patient=request.user).order_by('-created_at')
    return render(request, 'appointments/my_appointments.html', {'appointments': appointments})

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


def admin_required(view_func):
    """Custom decorator to allow only admin/superusers"""
    @login_required
    def wrapper(request, *args, **kwargs):
        profile = request.user.profile
        if request.user.is_superuser or profile.role == 'admin':
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("Access Denied.")
    return wrapper


@admin_required
def admin_dashboard(request):
    all_appointments = Appointment.objects.all().order_by('-created_at')
    total = all_appointments.count()
    pending = all_appointments.filter(status='pending').count()
    approved = all_appointments.filter(status='approved').count()
    completed = all_appointments.filter(status='completed').count()

    return render(request, 'appointments/admin_dashboard.html', {
        'appointments': all_appointments,
        'total': total,
        'pending': pending,
        'approved': approved,
        'completed': completed,
    })


@admin_required
def update_appointment(request, appointment_id, status):
    appointment = Appointment.objects.get(id=appointment_id)
    appointment.status = status
    appointment.save()

    # Send email notification
    try:
        send_appointment_email(appointment)
    except Exception as e:
        print(f"Email error: {e}")

    messages.success(request, f'Appointment marked as {status}.')
    return redirect('admin_dashboard')