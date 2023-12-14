from django.urls import path
from . import views

urlpatterns = [
    path("profile", views.profile, name="profile"),
    path(
        "edit_profile_picture", views.edit_profile_picture, name="edit_profile_picture"
    ),
    path("edit_profile_bio", views.edit_profile_bio, name="edit_profile_bio"),
    path("edit_user", views.edit_user, name="edit_user"),
]
