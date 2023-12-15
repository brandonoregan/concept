from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def post_home(request):
    recent_posts = Post.objects.order_by("-date")[0:5]

    return render(
        request, "posts/post_home.html", context={"recent_posts": recent_posts}
    )


# Class to create a post
class PostCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "posts/post_create.html"
    success_url = reverse_lazy("post_home")
    success_message = "Your post has been successfully created."

    # Set the author to the logged-in user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "posts/post_update.html"
    success_url = reverse_lazy("post_home")
    slug_field = "slug"
    slug_url_kwarg = "slug"
    success_message = "Your post has been successfully updated."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get("slug")
        post = Post.objects.get(slug=slug)
        context["post"] = post  # Add the post instance to the context
        return context


class PostDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("post_home")
    success_message = "Your post has been successfully deleted."

    def get_object(self, queryset=None):
        post_id = self.kwargs.get("pk")
        return Post.objects.get(pk=post_id)


@login_required
def post_single(request, slug):
    post = Post.objects.get(slug=slug)

    return render(
        request,
        "posts/post_single.html",
        {
            "post": post,
            "current_user": request.user,
        },
    )
