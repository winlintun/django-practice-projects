from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Task


class TaskHomeView(generic.ListView):
    model = Task
    template_name = "task/home.html"
    context_object_name = "tasks"


class TaskAddView(generic.CreateView):
    model = Task
    fields = ['title', 'description', 'due_date', 'assigned_to']
    success_url = "/"


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = "/"
    template_name = "task/delete.html"


class CompleteTaskView(View):
    template_name = 'task/complete.html'

    def get(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        return render(request, self.template_name, {'task': task})

    def post(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        if task.completed:
            task.completed = False
        else:
            task.completed = True
        task.save()
        return redirect('task:home')
