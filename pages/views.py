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
    services = [
        {'icon': '🫀', 'name': 'Cardiology', 'description': 'Heart and cardiovascular care'},
        {'icon': '🧠', 'name': 'Neurology', 'description': 'Brain and nervous system treatment'},
        {'icon': '🦷', 'name': 'Dentistry', 'description': 'Complete dental care services'},
        {'icon': '👁️', 'name': 'Ophthalmology', 'description': 'Eye care and vision treatment'},
        {'icon': '🤰', 'name': 'Maternity', 'description': 'Prenatal and postnatal care'},
        {'icon': '🦴', 'name': 'Orthopedics', 'description': 'Bone and joint treatments'},
        {'icon': '👶', 'name': 'Pediatrics', 'description': 'Healthcare for children'},
        {'icon': '🩺', 'name': 'General Medicine', 'description': 'General health consultations'},
    ]
    return render(request, 'pages/medical_services.html', {'services': services})
