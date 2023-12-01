from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Message
from .forms import MessageForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.db.models import Q, Max, OuterRef, Subquery
from apps.users.models import CustomUser
from collections import OrderedDict


from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

# When the inbox view is called I want to display the most recent message they've recieved
# When message is clicked on and form is submitted I want to display that specific message

# Get the most recent message and all preceding messages where the sender is the current user and the reciever id is equal to the sender


def inbox(request):
    current_user = request.user

    # Store all message where the current user is the receiver
    user_messages = Message.objects.filter(receiver=current_user).order_by("-id")

    # Store unique senders while maintaining the order of messages
    unique_senders = OrderedDict()
    for message in user_messages:
        if message.sender not in unique_senders:
            unique_senders[message.sender] = message

    # Extract unique messages from unique_senders while maintaining order
    unique_messages = list(unique_senders.values())

    # Get the most recent message received
    if user_messages:
        most_recent_message = unique_messages[0]

        message_thread = Message.objects.filter(
            Q(sender=current_user, receiver=most_recent_message.sender)
            | Q(sender=most_recent_message.sender, receiver=current_user)
        ).order_by("sent_at")

        return render(
            request,
            "messaging/inbox.html",
            {
                "user_messages": user_messages,
                "most_recent_message": most_recent_message,
                "message_thread": message_thread,
                "current_user": current_user,
                "unique_messages": unique_messages,
            },
        )
    
    # Get search query input data
    query = request.GET.get('q')
    if query:
        matched_users = CustomUser.objects.filter(username__icontains=query)
        return render(request, "messaging/inbox.html", {
            "user_messages": user_messages,
            "matched_users": matched_users,
            "current_user": current_user,
        })

    if request.method == 'POST':
        selected_username = request.POST.get('selected_username')
        if selected_username:
            selected_user = get_object_or_404(CustomUser, username=selected_username)

            conversation = Message.objects.filter(
            Q(sender=current_user, receiver=selected_user)
            | Q(sender=selected_user, receiver=current_user)).order_by("sent_at")

            return render(
            request,
            "messaging/inbox.html",
            {
                "user_messages": user_messages,
                "current_user": current_user,
                "selected_user": selected_user,
                "conversation": conversation,
            },
        )

    # Retrieve the message_id from the URL parameters
    message_id = request.GET.get("message_id")
    if message_id:
        message = get_object_or_404(Message, pk=message_id)
        return render(
            request,
            "messaging/inbox.html",
            {
                "user_messages": user_messages, "message": message},
        )
        # Now 'message' object is available in the inbox view if message_id is present in the URL

    return render(
        request,
        "messaging/inbox.html",
        {
            "user_messages": user_messages,
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
        return super().form_valid(form)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # Add additional context data here
    #     user_messages = Message.objects.all()
    #     context['user_messages'] = user_messages
    #     return context


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
    if message.read == False:
        message.read = True
        message.save()

    redirect_url = reverse("inbox")

    if message_id:
        redirect_url += f"?message_id={message_id}"

    return HttpResponseRedirect(redirect_url)
