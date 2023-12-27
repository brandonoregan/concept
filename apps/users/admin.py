from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "is_superuser")


admin.site.register(CustomUser, CustomUserAdmin)
