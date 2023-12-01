from django import forms
from .models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ProfileUpdateForm(forms.ModelForm):
    bio = forms.Textarea()
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields["bio"].widget.attrs["class"] = "bioInput"
        self.fields["bio"].label = "Bio:"
        self.fields["birthdate"].label = "Another Label Text"

        # Adding Crispy Forms functionality
        self.helper = FormHelper()
        self.helper.form_class = "updateProfile"
        self.helper.form_method = "post"
        self.helper.form_action = "profile"
        self.helper.add_input(Submit("submit", "Update", css_class="updateProfile"))

        # Populate the initial values of the form fields
        if self.instance.user:
            self.fields['bio'].initial = self.instance.bio
            self.fields['profile_picture'].initial = self.instance.profile_picture

    def save(self, commit=True):
        profile = super(ProfileUpdateForm, self).save(commit=False)
        profile.bio = self.cleaned_data['bio']
        profile.profile_picture = self.cleaned_data['profile_picture']

        # Update associated User model fields
        if profile.user:
            user = profile.user
            user.first_name = self.cleaned_data['first_name']  # Update User fields as needed
            user.last_name = self.cleaned_data['last_name']

            if commit:
                profile.save()
                user.save()

        return profile



# class ProfilePicForm(forms.ModelForm):
#     profile_picture = forms.ImageField(widget=forms.FileInput)

#     class Meta:
#         model = Profile
#         fields = ["profile_picture"]
