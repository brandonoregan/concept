from django.test import SimpleTestCase
from django.urls import reverse, resolve 
from apps.posts.views import post_home, PostCreate, PostUpdate, PostDeleteView, post_single

class TestUrls(SimpleTestCase):

    def test_post_home_url_resolves(self):
        url = reverse('post_home')
        self.assertEqual(resolve(url).func, post_home)

    def test_post_create_url_resolves(self):
        url = reverse('post_create')
        self.assertEqual(resolve(url).func.view_class, PostCreate)

    def test_post_single_url_resolves(self):
        url = reverse('post_single', args=["test-slug"])
        self.assertEqual(resolve(url).func, post_single)

    def test_post_update_url_resolves(self):
        url = reverse('post_update', kwargs={'slug':"test-slug"})
        self.assertEqual(resolve(url).func.view_class, PostUpdate)

    def test_post_delete_url_resolves(self):
        url = reverse('post_delete', args=[1])
        self.assertEqual(resolve(url).func.view_class, PostDeleteView)

    
