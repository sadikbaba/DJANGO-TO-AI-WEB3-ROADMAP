from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    display_name = models.CharField(max_length=200)
    bio = models.TextField()
    profile_picture = models.ImageField()
    date_of_birth = models.DateField()
    location = models.CharField(max_length=200)
    website = models.URLField()
    gender = models.CharField(max_length=100)
    privacy_settings = models.BooleanField()

  




