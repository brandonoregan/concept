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
from .utils import get_user_conversations, get_unique_participants, get_conversation_message_history
from django.db import transaction
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

# When the inbox view is called I want to display the most recent message they've recieved
# When message is clicked on and form is submitted I want to display that specific message

# Get the most recent message and all preceding messages where the sender is the current user and the reciever id is equal to the sender


def inbox(request, user_username=None):
    # Currently logged on user
    current_user = request.user

    # Get all user converstions in most recent order
    conversations = get_user_conversations(request.user) 

    # Get a list of unique participants from each conversation excluding user
    unique_participants = get_unique_participants(conversations, request.user)

    if user_username is None:
        selected_user = get_object_or_404(CustomUser, username='admin')
    else:
        selected_user = get_object_or_404(CustomUser, username=user_username)

    # Get conversation messages between two users
    conversation = get_conversation_message_history(current_user, selected_user)

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
                "selected_user": selected_user,
                'conversation': conversation,
            },
        )

    if request.method == "POST":
        selected_username = request.POST.get("selected_username")
        if selected_username:
            selected_user = get_object_or_404(CustomUser, username=selected_username)

            # Get conversation messages between two users
            conversation = get_conversation_message_history(current_user, selected_user)
        

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



@transaction.atomic
def replyMessage(request):
    if request.method == 'POST':
        # Get form data
        message_text = request.POST.get('message')
        receiver_username = request.POST.get('receiver_username')  # Assuming you have a hidden field for receiver in the form
        
        # Retrieve receiver
        receiver = get_object_or_404(CustomUser, username=receiver_username)

        # Create or retrieve conversation
        conversation = Conversation.objects.filter(participants=request.user).filter(participants=receiver).first()
        if not conversation:
            conversation = Conversation.objects.create()
            conversation.participants.add(request.user, receiver)

        # Create message object and associate it with the conversation
        message = Message.objects.create(
            sender=request.user,
            receiver=receiver,
            text=message_text,
            conversation=conversation
        )

        # Update the last_message timestamp of the conversation
        conversation.last_message = message.sent_at
        conversation.save()

        return redirect(reverse('inbox_with_user', kwargs={'user_username': receiver_username }))
    else:
        # Handle GET requests here if needed
        pass


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
