from django.contrib.auth.models import AbstractUser
from django.db import models
# from app.models import Department

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    signature = models.ImageField(upload_to='user_signatures/', null=True, blank=True)
    # department = models.ForeignKey('Department', on_delete=models.CASCADE)

    def __str__(self):
        return self.username
