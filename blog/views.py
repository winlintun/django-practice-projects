from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Tag, Category
from .forms import CommentForm, WritePost
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify


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

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['comments'] = self.object.comments.filter(active=True)
    #
    #     if self.request.method == "POST":
    #         context['comment_form'] = CommentForm(data=self.request.POST)
    #     else:
    #         context['comment_form'] = CommentForm()
    #         context['new_comment'] = self.object.comments.filter(active=False).order_by("-created_on")[:1]
    #
    #     return context
    #
    # def get_success_url(self) -> str:
    #     return reverse("blog:detail", kwargs={"slug": self.object.slug})
    #
    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     form = self.get_form()
    #
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)
    #
    # def form_valid(self, form):
    #     new_comment = form.save(commit=False)
    #     new_comment.post = self.object
    #     new_comment.save()
    #     return super().form_valid(form)


class PostUploadView(generic.CreateView):
    model = Post
    fields = ["title", "content", "image", "categories", "tags", "status"]
    template_name = "blog/form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(self.request.POST['title'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("blog:home")


def tag(request, name):
    return render(request, "blog/tag_content.html", {
        "data": Tag.objects.get(name=name),
    })


def category(request, name):
    return render(request, "blog/tag_content.html", {
        "data": Category.objects.get(name=name),
    })
