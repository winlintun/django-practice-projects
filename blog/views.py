from django.shortcuts import render
from django.views import generic
from .models import Post, Tag, Category
from .forms import CommentForm
from django.urls import reverse, reverse_lazy
from django.utils.text import slugify
from django.contrib.auth.mixins import LoginRequiredMixin


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "blog_list"

    def get_queryset(self):
        return Post.objects.filter(status=1)


class PostDetailView(generic.DetailView, generic.edit.FormMixin):
    model = Post
    template_name = "blog/detail.html"
    context_object_name = "post"
    form_class = CommentForm

    def get_object(self, queryset=None):
        post = super().get_object()
        post.count += 1
        post.save()
        return post


class PostUploadView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ["title", "content", "image", "categories", "tags", "status"]
    template_name = "blog/form.html"
    login_url = reverse_lazy("account:login")

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(self.request.POST['title'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("blog:home")


def explorer(request, name):
    data = None
    if Tag.objects.all().filter(name=name):
        data = Tag.objects.get(name=name)
    elif Category.objects.all().filter(name=name):
        data = Category.objects.get(name=name)

    return render(request, "blog/tag_content.html", {
        "data": data,
    })


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    fields = ["title", "content", "author", "image", "categories", "tags", "status"]
    context_object_name = "blog"
    template_name = "blog/blog_update.html"
