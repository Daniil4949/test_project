from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField(max_length=20, null=False, unique=True)
    email = models.CharField(max_length=30, null=False, unique=True)
    password = models.TextField(unique=True, null=False)

    def __str__(self):
        return self.username

# Create your models here.
