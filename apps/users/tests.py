from django.test import TestCase, Client
from django.urls import reverse
from .models import CustomUser, Post

# Create your tests here.


# class UsersModelsTests(TestCase):

    # @classmethod
    # def setUpTestData(cls):
    #     cls.user = CustomUser.objects.create(username='testuser', password='Password1', email="testuser@gmail.com")
    #     cls.post = Post.objects.create(
    #         author=cls.user,
    #         title='Test Post', 
    #         content='This is a test post'
    #     )


    # class URLTests(TestCase):
        
    #     def test_welcome_page(self):
    #         response = self.client.get('/')
    #         self.assertEqual(response.status_code, 200)

    #     def test_login(self):
    #         response = self.client.get('/login')
    #         self.assertEqual(response.status_code, 200)