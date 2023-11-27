from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


def home(request):
    return render(request, "posts/home.html")


# Class to create a post
class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "posts/post_create.html"
    success_url = reverse_lazy("home_page")


    # Set the author to the logged-in user
    def form_valid(self, form):
        form.instance.author = self.request.user  
        return super().form_valid(form)
