from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Message, Conversation
from .forms import MessageForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.db.models import Q, Max, OuterRef, Subquery
from apps.users.models import CustomUser
from collections import OrderedDict
from django.utils import timezone
from django.db.models import Max
from .utils import get_user_conversations, get_unique_participants

from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

# When the inbox view is called I want to display the most recent message they've recieved
# When message is clicked on and form is submitted I want to display that specific message

# Get the most recent message and all preceding messages where the sender is the current user and the reciever id is equal to the sender

# HELPER FUNCTIONS
# HELPER FUNCTIONS

def get_unique_sender(user_messages):
    """ """
    # Retrieve unique sender IDs from the user_messages queryset
    unique_senders_ids = user_messages.values_list("sender", flat=True).distinct()

    # Retrieve CustomUser objects for the unique sender IDs
    unique_senders = CustomUser.objects.filter(pk__in=unique_senders_ids)

    return unique_senders


def inbox(request):
    # Currently logged on user
    current_user = request.user

    # Get all user converstions in most recent order
    conversations = get_user_conversations(request.user) 

    # Get a list of unique participants from each conversation excluding user
    unique_participants = get_unique_participants(conversations, request.user)

    if request.method == "GET":

        # Get search query input data
        query = request.GET.get("q")
        if query:
            matched_users = CustomUser.objects.filter(username__icontains=query)
        else:
            matched_users = None

        # Retrieve the message_id from the URL parameters
        message_id = request.GET.get("message_id")
        if message_id:
            selected_message = get_object_or_404(Message, pk=message_id)
        else:
            selected_message = None

        return render(
            request,
            "messaging/inbox.html",
            {
                "current_user": current_user,
                "matched_users": matched_users,
                "selected_message": selected_message,
                "unique_participants": unique_participants,
            },
        )

    if request.method == "POST":
        selected_username = request.POST.get("selected_username")
        if selected_username:
            selected_user = get_object_or_404(CustomUser, username=selected_username)

            conversation = Message.objects.filter(
                Q(sender=current_user, receiver=selected_user)
                | Q(sender=selected_user, receiver=current_user)
            ).order_by("sent_at")

            return render(
                request,
                "messaging/inbox.html",
                {
                    "current_user": current_user,
                    "selected_user": selected_user,
                    "conversation": conversation,
                    "unique_participants": unique_participants,
                },
            )


    


class CreateMessage(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = "messaging/create_message.html"
    success_url = reverse_lazy("inbox")

    def form_valid(self, form):
        # Set the sender of the message to the current user
        form.instance.sender = self.request.user

        # Retrieve receiver and conversation logic
        receiver_id = form.instance.receiver.id

        receiver = get_object_or_404(CustomUser, id=receiver_id)  # Get receiver object

        # Your logic to create or retrieve a conversation
        conversation = Conversation.objects.filter(participants=self.request.user).filter(participants=receiver).first()

        if conversation:
            # Set the conversation for the message
            form.instance.conversation = conversation

            # Update the last_message timestamp of the conversation
            conversation.last_message = timezone.now()
            conversation.save()

        else:
            conversation = Conversation.objects.create()
            conversation.participants.add(self.request.user, receiver)
            form.instance.conversation = conversation


        return super().form_valid(form)


def replyMessage(request):
    """
    Creates a message object
    """
    reply = Message()
    return redirect("inbox")


def unopened(request, message_id):
    # Get message object that is associciated with message_id
    message = get_object_or_404(Message, pk=message_id)

    # Mark message as read if unread/False
    if message.unopened == False:
        message.unopened = True
        message.save()

    redirect_url = reverse("inbox")

    if message_id:
        redirect_url += f"?message_id={message_id}"

    return HttpResponseRedirect(redirect_url)
