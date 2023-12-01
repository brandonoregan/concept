from django.urls import path
from . import views

urlpatterns = [
    path("profile/", views.edit_profile, name="profile"),
]
