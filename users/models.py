from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField()
    profile_pic = models.ImageField(upload_to='profile_pics/', default='default_profile.jpg')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
