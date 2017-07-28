from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from task.forms import NewTaskForm

# Create your views here.
def new_task(request):
    user = request.user
    if request.method == 'POST':
        form = NewTaskForm(request.POST or None, {'username':user.username})
        if form.is_valid():
            task = form.save()
            task.profile = form.cleaned_data.get('profile', None)
            task.task_type = form.cleaned_data.get('task_type', None)
            task.datetime = form.cleaned_data.get('datetime')
            task.duration = form.cleaned_data.get('duration')
            task.save()
            return redirect('home')
    else:
        form = NewTaskForm()

    return render(request, 'task/new_task.html', {'form':form})
