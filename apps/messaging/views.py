from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Message
from .forms import MessageForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.db.models import Q


from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

# When the inbox view is called I want to display the most recent message they've recieved
# When message is clicked on and form is submitted I want to display that specific message 

# Get the most recent message and all preceding messages where the sender is the current user and the reciever id is equal to the sender



def inbox(request):
    current_user = request.user
    # Store all message where the current user is the receiver 
    user_messages = Message.objects.filter(receiver=current_user).order_by('-id')
    
    # Get the most recent message received
    if user_messages:
        display_message = user_messages[0]
        display_message.sender

        message_thread = Message.objects.filter(Q(sender=current_user, receiver=display_message.sender) | Q(sender=display_message.sender, receiver=current_user)).order_by('sent_at')

        return render(request, "messaging/inbox.html", {
        "user_messages": user_messages,
        "display_message": display_message,
        "message_thread": message_thread,
        })
        

    # Retrieve the message_id from the URL parameters
    message_id = request.GET.get("message_id")
    if message_id:
        message = get_object_or_404(Message, pk=message_id)
        return render(
            request,
            "messaging/inbox.html",
            {"user_messages": user_messages, "message": message},
        )
        # Now 'message' object is available in the inbox view if message_id is present in the URL

    return render(request, "messaging/inbox.html", {
        "user_messages": user_messages,
        })


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
