from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def post_home(request):
    recent_posts = Post.objects.order_by('-date')[0:5]
    for post in recent_posts:
        print(post.id)

    return render(request, "posts/post_home.html", context={"recent_posts": recent_posts})


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


# TODO: Create a slug url when on specific post page
def post_single(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post=post)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)  # TODO add comment form
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return redirect("post_page", post_id=post_id)
    else:
        comment_form = CommentForm()  # TODO add comment form

    return render(
        request,
        "posts/post_single.html",
        {
            "post": post,
            "comments": comments,
            "comment_form": comment_form,
        },
    )
