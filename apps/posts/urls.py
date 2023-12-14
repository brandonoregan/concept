from django.urls import path
from . import views

urlpatterns = [
    path("post_home", views.post_home, name="post_home"),
    path("post_create", views.PostCreate.as_view(), name="post_create"),
    path("post/<slug:slug>/", views.post_single, name="post_single"),
    path(
        "post-update/<slug:slug>/update", views.PostUpdate.as_view(), name="post_update"
    ),
    path(
        "post-delete/<int:pk>/delete/",
        views.PostDeleteView.as_view(),
        name="post_delete",
    ),
]
