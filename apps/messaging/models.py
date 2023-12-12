from django.db import models
from apps.users.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Q

# Create your models here.


class Conversation(models.Model):
    participants = models.ManyToManyField(CustomUser, related_name="conversations")
    last_message = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ", ".join(str(participant) for participant in self.participants.all())


class Message(models.Model):
    sender = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="sent_messages"
    )
    receiver = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="received_messages"
    )
    text = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    conversation = models.ForeignKey(
        Conversation, on_delete=models.CASCADE, related_name="messages"
    )

    # Provides a string representation of an object
    def __str__(self):
        return f"{self.sender} -> {self.receiver}: {self.text}"

# @receiver(post_save, sender=CustomUser)
# def welcome_message(sender, instance, created, **kwargs):
#     if created:

#         admin = CustomUser.objects.get(username='admin')

#         welcome_text = 'Welcome to your inbox! Use the search bar to find people to connect with, or even chat to me!'

#         # Create or retrieve conversation
#         conversation = Conversation.objects.filter(participants=request.user).filter(participants=admin).first()

#         if not conversation:
#             conversation = Conversation.objects.create()
#             conversation.participants.add(request.user, receiver)

#         message = Message.objects.create(
#             sender=admin,
#             receiver=instance,
#             text=welcome_text,
#             conversation=conversation
#         )

#         # Update the last_message timestamp of the conversation
#         conversation.last_message = message.sent_at
#         conversation.save()
