from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home, name="home_page"),
    path("post_create", views.PostCreate.as_view(), name="post_create"),
    # path("post/<int:post_id>/", views.post_page, name="post_page"),
]
