from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Company, Application
from .tasks import send_application_email


@receiver(post_save, sender=Application)
def application_created(sender, instance, created, **kwargs):
    if created:
        send_application_email.delay(
            instance.applicant.email,
            instance.job.company.name,
            instance.job.title,
        )


@receiver(post_save, sender=Company)
def company_created(sender, instance, created, **kwargs):
    if created:
        print(f"{instance.name} was created successfully")
