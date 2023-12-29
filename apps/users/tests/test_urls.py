from django.test import SimpleTestCase
from django.urls import reverse, resolve 
from apps.users.views import welcome, LoginUser, RegisterUser, LogoutUser
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView

class TestUrls(SimpleTestCase):

    def test_welcome_url_resolves(self):
        self.assertEqual(resolve(reverse('welcome')).func, welcome)

    def test_login_user_url_resolves(self):
        self.assertEqual(resolve(reverse('login_user')).func.view_class, LoginUser)

    def test_resgister_url_resolves(self):
        self.assertEqual(resolve(reverse('register_user')).func.view_class, RegisterUser)

    def test_logout_url_resolves(self):
        self.assertEqual(resolve(reverse('logout_user')).func.view_class, LogoutUser)

    def test_password_reset_url_resolves(self):
        self.assertEqual(resolve(reverse('password-reset')).func.view_class, PasswordResetView)

    def test_password_reset_done_url_resolves(self):
        self.assertEqual(resolve(reverse('password_reset_done')).func.view_class, PasswordResetDoneView)

    def test_password_reset_complete_url_resolves(self):
        self.assertEqual(resolve(reverse('password_reset_complete')).func.view_class, PasswordResetCompleteView)

