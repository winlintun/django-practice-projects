from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from blog.models import Post


@login_required()
def home(request, username):
    user = get_object_or_404(User, username=username)
    blogs = Post.objects.all().filter(status=1).order_by("-created_on")[:3]
    context = {
        "user": user,
        "blogs": blogs,
    }
    return render(request, "portfolio/home.html", context)
