# test_email.py

from django.core.mail import send_mail
from django.conf import settings

send_mail(
    'Test Email',
    'This is a test email.',
    settings.DEFAULT_FROM_EMAIL,
    ['coffeehub@gmail.com'],
    fail_silently=False,
)
