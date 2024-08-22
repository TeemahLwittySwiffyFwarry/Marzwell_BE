# utils.py
from django.core.mail import send_mail
from django.conf import settings

def send_contact_email(subject, message, from_email, recipient_list):
    send_mail(
        subject,
        message,
        from_email,
        recipient_list,
        fail_silently=False,
    )
