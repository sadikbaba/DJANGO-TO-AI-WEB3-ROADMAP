from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to="photos/post")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=100)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to="photos/profiles")
    date_of_birth = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=200)
    website = models.URLField()
    gender = models.CharField(max_length=100)
    privacy_settings = models.BooleanField(default=False)
