from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']


class WritePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "image", "categories", "tags", "status"]

