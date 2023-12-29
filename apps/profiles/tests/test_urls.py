# from django.test import SimpleTestCase
# from django.urls import reverse, resolve 
# from apps.messaging.views import inbox, create_message

# class TestUrls(SimpleTestCase):

#     def test_inbox_url_resolves(self):
#         url = reverse('inbox')
#         print(resolve(url))
#         self.assertEqual(resolve(url).func, inbox)

#     def test_inbox_with_user_url_resolves(self):
#         username = 'testuser'
#         url = reverse('inbox_with_user', kwargs={'user_username': username})
#         print(resolve(url))
#         self.assertEqual(resolve(url).func, inbox)
#         self.assertEqual(resolve(url).kwargs['user_username'], username)
    
    
#     def test_create_message_url_resolves(self):
#         url = reverse('create_message')
#         print(resolve(url))
#         self.assertEqual(resolve(url).func, create_message)

