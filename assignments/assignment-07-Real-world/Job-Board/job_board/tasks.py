from celery import shared_task
from django.core.mail import send_mail

@shared_task
def say_hello():
    print("Hello from Celery!")


@shared_task
def send_application_email(email, company, job):
    send_mail(
        subject=f"Application received for {job}",
        message=f"Thank you for applying to {company}.",
        from_email="noreply@jobboard.com",
        recipient_list=[email],
    )