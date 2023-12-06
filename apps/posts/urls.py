from django.urls import path
from . import views

urlpatterns = [
    path("post_home", views.post_home, name="post_home"),
    path("post_create", views.PostCreate.as_view(), name="post_create"),
    path("post/<int:post_id>/", views.post_single, name="post_thread"),
]
