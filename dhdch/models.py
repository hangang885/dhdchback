from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.TextField(max_length=10,unique=True)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
