# from django.test import TestCase
# from apps.messaging.models import Message, Conversation
# from apps.users.models import CustomUser

# # Create your tests here.


# class TestMessagingModels(TestCase):

#     @classmethod
#     def setUpTestData(cls):

#         cls.user1 = CustomUser.objects.create(username='testuser1', password='Password1', email="testuser1@gmail.com")

#         cls.user2 = CustomUser.objects.create(username='testuser2', password='Password2', email="testuser2@gmail.com")

#         cls.conversation = Conversation.objects.create()
#         cls.conversation.participants.add(cls.user1, cls.user2)

#         cls.message = Message.objects.create(
#             sender=cls.user1,
#             receiver=cls.user2, 
#             text='This is about testing',
#             conversation=cls.conversation
#         )

#         print("Message Sender:", cls.message.sender, "Conversation", cls.message.conversation)
        

#     def test_message_model(self):
#         message = Message.objects.get(id=1)
#         excepted_sender = f'{message.sender}'
#         excepted_receiver = f'{message.receiver}'
#         excepted_test = f'{message.text}'
#         self.assertEqual(excepted_sender, 'testuser1')
#         self.assertEqual(excepted_receiver, 'testuser2')
#         self.assertEqual(excepted_test, 'This is about testing')