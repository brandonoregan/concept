from django.db import models
from apps.users.models import CustomUser
from django.core.validators import MinLengthValidator
from django.utils.text import slugify


# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True
    )
    title = models.CharField(max_length=150)
    about = models.CharField(max_length=300, default="...")
    content = models.TextField(validators=[MinLengthValidator(10)])
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, max_length=150)
    post_image = models.ImageField(
        upload_to="post_images/", blank=True, null=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    author = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
