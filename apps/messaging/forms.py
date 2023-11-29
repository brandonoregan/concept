from django import forms
from .models import Message
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["receiver", "subject", "content"]
