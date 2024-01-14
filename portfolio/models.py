from django.db import models
from django.contrib.auth.models import User


class WhatIDo(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    image = models.ImageField(default="whatido", null=True, blank=True, help_text="Ok add icon photo")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} what i do -- {self.title}"


class MySkill(models.Model):
    name = models.CharField(max_length=30)
    level = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} + {self.level} %"


class MyExperience(models.Model):
    exp = models.IntegerField(default=0)
    complete_project = models.IntegerField(default=0)
    happy_customer = models.IntegerField(default=0)
    award = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.exp} exp {self.complete_project} projects"


class MyWork(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="projects", default="")
    project_type = models.CharField(max_length=200, blank=True, null=True)
    project_link = models.CharField(max_length=2080, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class MyEducation(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.CharField(help_text="2013", max_length=10)
    end_date = models.CharField(help_text="2014", max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class MyWorkingExperiences(models.Model):
    title = models.CharField(max_length=200)
    position = models.CharField(max_length=200, null=True, blank=True)
    start_date = models.CharField(help_text="2013", max_length=10)
    end_date = models.CharField(help_text="2014", max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
