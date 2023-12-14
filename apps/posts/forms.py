from django import forms
from .models import Post, Comment, Like, Tag
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_action = "post_create"

        self.helper.add_input(Submit("submit", "Submit", css_class="submitButton"))

    class Meta:
        model = Post
        fields = ["title", "about", "content", "post_image"]
