from django.contrib import admin
from .models import Post
from django.utils.text import slugify


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

    list_display = (
        "title",
        "author",
        "date",
    )

    def save_model(self, request, obj, form, change):
        obj.slug = slugify(obj.title)
        super().save_model(request, obj, form, change)


admin.site.register(Post, PostAdmin)
