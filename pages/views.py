from django.shortcuts import render

def about(request):
    return render(request, 'pages/about.html')


def services(request):
    return render(request, 'pages/services.html')


def facilities(request):
    return render(request, 'pages/facilities.html')


def emergency(request):
    return render(request, 'pages/emergency.html')


def contact(request):
    return render(request, 'pages/contact.html')


def medical_services(request):
    return render(request, 'pages/medical_services.html')


