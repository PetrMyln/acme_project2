from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

class CustomUser(AbstractUser):
    birthday = models.DateField(null=True)
    bio = models.TextField(null=True)
