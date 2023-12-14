from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def post_home(request):
    recent_posts = Post.objects.order_by("-date")[0:5]

    return render(
        request, "posts/post_home.html", context={"recent_posts": recent_posts}
    )


# Class to create a post
class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "posts/post_create.html"
    success_url = reverse_lazy("post_home")

    # Set the author to the logged-in user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@login_required
def post_single(request, slug):
    post = Post.objects.get(slug=slug)

    return render(
        request,
        "posts/post_single.html",
        {
            "post": post,
        },
    )
