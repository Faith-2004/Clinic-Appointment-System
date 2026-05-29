from django.core.mail import send_mail
from django.conf import settings


def send_appointment_email(appointment):
    patient_email = appointment.patient.email
    doctor_name = appointment.doctor.name
    date = appointment.appointment_date
    time = appointment.appointment_time

    if not patient_email:
        return  # skip if patient has no email

    if appointment.status == 'approved':
        subject = '✅ Appointment Approved - Clinic System'
        message = f"""
Dear {appointment.patient.username},

Your appointment has been APPROVED!

Details:
  Doctor   : Dr. {doctor_name}
  Date     : {date}
  Time     : {time}

Please arrive 10 minutes early.

Regards,
Clinic System
        """

    elif appointment.status == 'cancelled':
        subject = '❌ Appointment Cancelled - Clinic System'
        message = f"""
Dear {appointment.patient.username},

Unfortunately your appointment has been CANCELLED.

Details:
  Doctor   : Dr. {doctor_name}
  Date     : {date}
  Time     : {time}

Please contact us to reschedule.

Regards,
Clinic System
        """
    else:
        return  # only send for approved/cancelled

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [patient_email],
        fail_silently=False,
    )