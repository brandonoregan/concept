from django.db import models
from apps.users.models import CustomUser


class Conversation(models.Model):
    participants = models.ManyToManyField(
        CustomUser, related_name="conversations"
    )
    last_message = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ", ".join(
            str(participant) for participant in self.participants.all()
        )


class Message(models.Model):
    sender = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="sent_messages"
    )
    receiver = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="received_messages"
    )
    text = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    receiver_read = models.BooleanField(default=False)
    sender_read = models.BooleanField(default=True)
    conversation = models.ForeignKey(
        Conversation, on_delete=models.CASCADE, related_name="messages"
    )

    # Provides a string representation of an object
    def __str__(self):
        return f"{self.sender} -> {self.receiver}: {self.text}"
