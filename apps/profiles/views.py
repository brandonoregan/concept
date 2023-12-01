from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ProfileUpdateForm
from .models import Profile

# Create your views here.


def edit_profile(request):
    if request.method == "POST":
        if "info_form" in request.POST:
            info_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
            if info_form.is_valid():
                info_form.save()

    return render(
        request,
        "profiles/edit_profile.html",
        context={
            "info_form": ProfileUpdateForm(instance=request.user.profile),
        },
    )
