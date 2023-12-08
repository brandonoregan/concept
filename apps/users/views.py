from django.shortcuts import render
from django.shortcuts import render
from .forms import CreateUser
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from apps.profiles.models import Profile
from apps.messaging.models import Message
from .models import CustomUser

# Create your views here.


# View for initial website page
def welcome(request):
    return render(request, "users/welcome.html")


class LoginUser(SuccessMessageMixin, LoginView):
    template_name = "users/login_user.html"
    success_url = reverse_lazy("post_home")
    success_message = "You were successfully logged in."


class LogoutUser(SuccessMessageMixin, LogoutView):
    next_page = reverse_lazy("welcome")

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        # Add a success message
        messages.success(self.request, ("You were successfully logged out."))
        return response


class RegisterUser(SuccessMessageMixin, CreateView):
    template_name = "users/register_user.html"  # Designate the template to display view
    form_class = CreateUser  # From which form shouldd this view be created
    success_message = (
        "Your profile was created successfully"  # Following successful registration
    )
    success_url = reverse_lazy("login_user")  # Redirected page or view trigger
    # authentication_form = CustomLoginForm

    # Login registered user on correct form validation
    def form_valid(self, form):
        # Save the user instance and get the user object
        user = form.save()

        # Create a Profile instance linked to the user
        Profile.objects.create(user=user)

        # Log in the user
        login(self.request, user)

        # # Fetch the admin Custom User Object
        # admin = CustomUser.objects.get(username='admin')

        # # Create a Message object
        # Message.objects.create(sender=admin, receiver=user, text='Welcome to your inbox, use the search bar to find people to connect with!')

        return super().form_valid(form)
