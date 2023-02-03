from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import *
from .forms import TaskForm, Task


# Create your views here.
def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {'tasks': tasks, 'form': form}
    return render(request, 'TODOAPP/list.html', context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {"form": form, "task": task}

    return render(request, 'TODOAPP/update.html', context)


def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect("/")

    context = {"item": item, "task": task}
    return render(request, "TODOAPP/delete.html", context)
