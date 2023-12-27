from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


# Inherits from built in User class
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)

    class Meta:
        managed = True
        app_label = 'users'
