from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from .forms import ProfileForm, ProfilePicForm, EditUserForm
from .models import Profile
from apps.users.models import CustomUser

# Create your views here.


def edit_profile(request):
    # Check if the logged in user has a profile picture available
    if request.user.profile.profile_picture:
        profile_picture = request.user.profile.profile_picture
    else:
        profile_picture = None

    if request.method == "POST":
        print('Heyp')
        if "pic_form" in request.POST:
            print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
            print('FIRST STEP ')
            print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
            pic_form = ProfilePicForm(
                request.POST, request.FILES, instance=request.user.profile
            )
            if pic_form.is_valid():
                print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
                print('VALID ')
                print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
                pic_form.save()
            else:
                print(pic_form.errors)
        elif "info_form" in request.POST:
            info_form = ProfileForm(request.POST, instance=request.user.profile)
            if info_form.is_valid():
                info_form.save()
        return render(
        request,
        "profiles/edit_profile.html",
        context={
            'profile_picture': profile_picture,
            "info_form": ProfileForm(instance=request.user.profile),
            "pic_form": ProfilePicForm(instance=request.user.profile),
        },
    )
    return render(
        request,
        "profiles/edit_profile.html",
        context={
            'profile_picture': profile_picture,
            "info_form": ProfileForm(instance=request.user.profile),
            "pic_form": ProfilePicForm(instance=request.user.profile),
        },
    )

def edit_user(request):
    form = EditUserForm()

    if request.method == "POST":
        edit_user_form = EditUserForm(request.POST, instance=request.user)

        if edit_user_form.is_valid():
            edit_user_form.save()

    return render(request, "profiles/edit_user.html", context={
        "form": form
    })