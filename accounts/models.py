from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField()
    username = models.CharField(max_length=15, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
# Create your models here.
