from django.urls import path
from . import views
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)


urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("login/", views.LoginUser.as_view(), name="login_user"),
    path("register/", views.RegisterUser.as_view(), name="register_user"),
    path("logout/", views.LogoutUser.as_view(), name="logout_user"),
    # Password recovery url patterns
    path(
        "password-reset/",
        PasswordResetView.as_view(
            template_name="users/password_recovery/password_reset.html"
        ),
        name="password-reset",
    ),
    path(
        "password-reset/done/",
        PasswordResetDoneView.as_view(
            template_name="users/password_recovery/done_password_reset.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="users/password_recovery/confirm_password_reset.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        PasswordResetCompleteView.as_view(
            template_name="users/password_recovery/complete_password_reset.html"
        ),
        name="password_reset_complete",
    ),
]
