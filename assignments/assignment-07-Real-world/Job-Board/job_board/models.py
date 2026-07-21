from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    logo = models.ImageField(upload_to="company_logos/", blank=True)
    website = models.URLField(blank=True)
    location = models.CharField(max_length=200, blank=True)
    industry = models.CharField(max_length=200)

    def __str__(self):
        return self.name