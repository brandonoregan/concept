from django.contrib import admin
from apps.users.models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "is_superuser"
    )


admin.site.register(CustomUser, CustomUserAdmin)