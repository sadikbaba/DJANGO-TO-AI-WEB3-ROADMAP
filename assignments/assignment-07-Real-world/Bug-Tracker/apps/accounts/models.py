from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(blank=True)
    website = models.URLField(blank=True)
    location = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_atm = models.DateTimeField(auto_now=True)

    def full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"  # i dont know what is .strip() explain to me the i will use it
