from crispy_forms.helper import FormHelper
from django import forms
from crispy_forms.layout import Layout, Submit
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


# Create a user creation form to keep crsipy form code in forms.py
class CreateUser(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = "registerForm"
        self.helper.form_method = "post"
        self.helper.form_action = "register_user"
        self.helper.add_input(Submit("submit", "Submit", css_class="registerButton"))

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2"]
