from django.shortcuts import render, redirect
from .models import *
from .forms import *


def home(request):
    entries = Entry.objects.order_by('-date_posted')

    context = {'entries' : entries}

    return render(request, 'acc/main.html', context)

def add(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EntryForm()

    context = {'form' : form}

    return render(request, 'acc/write.html', context)

def delete_entry(request, entry):
    Entry.objects.get(text= entry).delete()
    return redirect('home')

def edit_entry(request, id):
    entry = Entry.objects.get(id=id)
    form1 = EntryForm(instance=entry)
    if request.method == 'POST':
        form1 = EntryForm(request.POST, instance=entry)
        if form1.is_valid():
            form1.save()
            return redirect('/')
    context = {'form1': form1}
    return render(request, 'acc/edit.html', context)

def Tasks(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'tasks': tasks, 'form': form}
    return render(request, 'acc/index.html', context)

def delete_task(request, task):
    Task.objects.get(id=task).delete()
    return redirect('Tasks')

def cross(request, id):
    tasks = Task.objects.get(pk=id)
    tasks.completed = True
    tasks.save()
    return redirect('Tasks')

def uncross(request, id):
    tasks = Task.objects.get(pk=id)
    tasks.completed = False
    tasks.save()
    return redirect('Tasks')

def edit(request, id):
    task = Task.objects.get(id=id)
    form1 = TaskForm(instance=task)
    if request.method == 'POST':
        form1 = TaskForm(request.POST, instance=task)
        if form1.is_valid():
            form1.save()
            return redirect('Tasks')
    context = {'form1': form1}
    return render(request, 'acc/edit.html', context)