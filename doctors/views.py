from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .models import Doctor


def admin_required(view_func):
    @login_required
    def wrapper(request, *args, **kwargs):
        if request.user.is_superuser or request.user.profile.role == 'admin':
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("Access Denied.")
    return wrapper


@admin_required
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/doctor_list.html', {'doctors': doctors})


@admin_required
def add_doctor(request):
    if request.method == 'POST':
        name = request.POST['name']
        specialization = request.POST['specialization']
        phone = request.POST['phone']
        email = request.POST['email']
        available = request.POST.get('available') == 'on'

        Doctor.objects.create(
            name=name,
            specialization=specialization,
            phone=phone,
            email=email,
            available=available
        )
        messages.success(request, f'Dr. {name} added successfully!')
        return redirect('doctor_list')

    return render(request, 'doctors/add_doctor.html')


@admin_required
def edit_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)

    if request.method == 'POST':
        doctor.name = request.POST['name']
        doctor.specialization = request.POST['specialization']
        doctor.phone = request.POST['phone']
        doctor.email = request.POST['email']
        doctor.available = request.POST.get('available') == 'on'
        doctor.save()
        messages.success(request, f'Dr. {doctor.name} updated successfully!')
        return redirect('doctor_list')

    return render(request, 'doctors/edit_doctor.html', {'doctor': doctor})


@admin_required
def delete_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    doctor.delete()
    messages.success(request, 'Doctor deleted successfully!')
    return redirect('doctor_list')

@login_required
def browse_doctors(request):
    doctors = Doctor.objects.filter(available=True)
    return render(request, 'doctors/browse_doctors.html', {'doctors': doctors})