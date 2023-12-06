from django.urls import path
from . import views

urlpatterns = [
    path("profile", views.profile, name="profile"),
    path("edit_profile", views.edit_profile, name="edit_profile"),
    path("edit_user", views.edit_user, name="edit_user"),
]
