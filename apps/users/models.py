from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Inherits from built in User class
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)

    class Meta:
        managed = True


# Provide unique related_name for groups and user_permissions
CustomUser._meta.get_field('groups').remote_field.related_name = 'custom_user_groups'
CustomUser._meta.get_field('user_permissions').remote_field.related_name = 'custom_user_user_permissions'