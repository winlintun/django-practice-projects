from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS = (
        (0, "Draft"),
        (1, "Publish")
    )

    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="img/images", blank=True, null=True)
    categories = models.ManyToManyField(Category, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    count = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_on']


class Comment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} by {self.post}"