from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    # Add any other fields you need for authentication and profile information

    def __str__(self):
        return self.username
