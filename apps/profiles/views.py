from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import UpdateView
from .forms import ProfileForm, ProfilePicForm, EditUserForm
from .models import Profile
from apps.users.models import CustomUser
from apps.posts.models import Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def profile(request):
    # Check if the logged in user has a profile picture available
    if request.user.profile.profile_picture:
        profile_picture = request.user.profile.profile_picture
    else:
        profile_picture = None

    if Post.objects.filter(author=request.user).exists():
        user_posts = Post.objects.filter(author=request.user)
    else:
        user_posts = None

    return render(
        request,
        "profiles/profile.html",
        context={
            "profile_picture": profile_picture,
            "current_user": request.user,
            "user_posts": user_posts,
        },
    )


@login_required
def edit_user(request):
    form = EditUserForm()

    if request.method == "POST":
        edit_user_form = EditUserForm(request.POST, instance=request.user)

        if edit_user_form.is_valid():
            edit_user_form.save()

    return render(request, "profiles/edit_user.html", context={"form": form})


@login_required
def edit_profile(request):
    # Need to update models in new form and replace the profile view so that it renders those updates after submission
    if request.method == "POST":
        if "pic_form" in request.POST:
            pic_form = ProfilePicForm(
                request.POST, request.FILES, instance=request.user.profile
            )

            if pic_form.is_valid():
                pic_form.save()
                messages.success(
                    request, ("Your profile picture was successfully updated.")
                )

        elif "info_form" in request.POST:
            info_form = ProfileForm(request.POST, instance=request.user.profile)
            if info_form.is_valid():
                info_form.save()
                messages.success(request, ("Your bio was successfully updated."))

        return redirect(reverse("profile"))

    return render(
        request,
        "profiles/edit_profile.html",
        context={
            "info_form": ProfileForm(instance=request.user.profile),
            "pic_form": ProfilePicForm(instance=request.user.profile),
        },
    )
