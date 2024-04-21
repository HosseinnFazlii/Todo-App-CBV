from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Task
from django.views.generic.list import ListView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.views import View

from .forms import TaskUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class Tasklist(LoginRequiredMixin,ListView):
    model=Task
    context_object_name = "tasks"
    template_name = "todo/list_task.html"

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
    
#create view
class Createview(LoginRequiredMixin,CreateView):
    model = Task 
    template_name = 'todo/list_task.html'
    fields=['title']
    success_url=reverse_lazy("todo:task_list")
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Createview, self).form_valid(form)
    
#updateview
class Updateview(LoginRequiredMixin,UpdateView):
    model = Task
    success_url=reverse_lazy("todo:task_list")
    template_name = 'todo/list_task.html'
    form_class = TaskUpdateForm
    template_name = "todo/update_task.html"

#complete task view

class Completeview(LoginRequiredMixin,View):
    model = Task
    success_url=reverse_lazy("todo:task_list")

    def get(self, request, *args, **kwargs):
        object = Task.objects.get(id=kwargs.get("pk"))
        object.complete = True
        object.save()
        return redirect(self.success_url)

#delet view
class Deleteview(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name = "tasks"
    success_url=reverse_lazy("todo:task_list") 
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)