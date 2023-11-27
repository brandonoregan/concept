from django.db import models
from apps.users.models import CustomUser
from django.core.validators import MinLengthValidator
from django.utils.text import slugify


# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption
    
class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=150)
    about = models.CharField(max_length=300, default="...")
    content = models.TextField(validators=[MinLengthValidator(10)])
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, max_length=150)
    post_image = models.ImageField(upload_to="post_images/", blank=True, null=True)
    likes = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag)



    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)


# Model for each like on posts
class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)



