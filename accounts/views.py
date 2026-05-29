from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile

def home(request):
    return render(request, 'home.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken!')
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password1)
        Profile.objects.create(user=user, phone=phone, role='patient')
        messages.success(request, 'Account created! Please login.')
        return redirect('login')

    return render(request, 'accounts/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome, {user.username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password!')

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    profile, created = Profile.objects.get_or_create(
        user=request.user,
        defaults={'role': 'admin' if request.user.is_superuser else 'patient'}
    )
    return render(request, 'accounts/dashboard.html', {'profile': profile})

    from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden


def admin_required(view_func):
    @login_required
    def wrapper(request, *args, **kwargs):
        if request.user.is_superuser or request.user.profile.role == 'admin':
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("Access Denied.")
    return wrapper


@admin_required
def patient_list(request):
    patients = Profile.objects.filter(role='patient').select_related('user')
    return render(request, 'accounts/patient_list.html', {'patients': patients})


@admin_required
def delete_patient(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    messages.success(request, 'Patient deleted successfully!')
    return redirect('patient_list')