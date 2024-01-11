from django.shortcuts import render
from django.views import generic
from .models import Post
from .forms import CommentForm
from django.urls import reverse


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
