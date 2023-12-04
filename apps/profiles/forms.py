from django import forms
from .models import Profile
from django.urls import reverse_lazy
from apps.users.models import CustomUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio"]

        widgets = {
            "bio": forms.Textarea(
                attrs={
                    "placeholder": "Tell us a little about yourself...",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'bioInput'  # CSS class for the form
        self.helper.label_class = ''  # CSS class for the labels
        self.helper.field_class = ''  # CSS class for the input fields

        self.helper.layout = Layout(
            'bio',  # Define fields here in the desired order
            Submit('info_form', 'Update Bio')  # Adding a submit button
        )


class ProfilePicForm(forms.ModelForm):
    profile_picture = forms.ImageField(widget=forms.FileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = "profile_pic_button"
        self.helper.form_method = "post"
        self.helper.form_action = reverse_lazy("profile")
        self.helper.add_input(Submit("pic_form", "Upload"))
        
    class Meta:
        model = Profile
        fields = ["profile_picture"]
    
    

class EditUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'edit_user'
        self.helper.form_class = 'edit_user'
        self.helper.form_method = 'post'
        self.helper.form_action = 'edit_user'

        self.helper.add_input(Submit('submit', 'Submit'))