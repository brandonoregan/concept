from django.contrib import admin
from apps.profiles.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
    )



admin.site.register(Profile, ProfileAdmin)