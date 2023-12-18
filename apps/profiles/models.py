from django.db import models
from apps.users.models import CustomUser


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    short_bio = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to="profile_pics/", blank=True, null=True
    )

    class Meta:
        managed = True
