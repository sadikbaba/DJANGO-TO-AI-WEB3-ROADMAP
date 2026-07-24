from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Company


@receiver(post_save, sender=Company)
def company_created(sender, instance, created, **kwargs):
    if created:
        print(f"{instance.name} was created successfully")
