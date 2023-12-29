from django.test import SimpleTestCase
from django.urls import reverse, resolve 
from apps.profiles.views import profile, edit_profile_picture, edit_profile_bio, edit_user

class TestUrls(SimpleTestCase):

    def test_profile_url_resolves(self):
        url = reverse("profile")
        print(resolve(url))
        self.assertEqual(resolve(url).func, profile)

    def test_edit_profile_picture_url_resolves(self):
        self.assertEqual(resolve(reverse("edit_profile_picture")).func, edit_profile_picture)

    def test_edit_profile_bio_url_resolves(self):
        self.assertEqual(resolve(reverse("edit_profile_bio")).func, edit_profile_bio)

    def test_edit_user_url_resolves(self):
        self.assertEqual(resolve(reverse('edit_user')).func, edit_user)


    

