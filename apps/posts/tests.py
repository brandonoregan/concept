from django.test import TestCase
from .models import Post
from apps.users.models import CustomUser

# Create your tests here.


class PostsModelsTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.objects.create(username='testuser', password='Password1', email="testuser@gmail.com")
        cls.post = Post.objects.create(
            author=cls.user,
            title='Test Post', 
            about='This is about testing',
            content='This is a test post',
        )

    def test_post_content(self):
        post = Post.objects.get(id=1)
        excepted_author = f'{post.author}'
        excepted_title = f'{post.title}'
        excepted_content = f'{post.content}'
        self.assertEqual(excepted_author, 'testuser')
        self.assertEqual(excepted_title, 'Test Post')
        self.assertEqual(excepted_content, 'This is a test post')