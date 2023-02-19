from django.shortcuts import render, redirect
from .models import Todo
from .models import Categorie
from .forms import TaskForm


def todo(request):
    todo = Todo.objects.all()
    return render(request, "index.html", {"todo": todo})


def task(request):
    if request.method == "GET":
        form = TaskForm()
        return render(request, 'add.html', {'form': form})

    if request.method == "POST":

        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('todo')


def categorie(request):
    category = Categorie.objects.all()
    context = {"categorie": category}
    return render(request, "index.html", context)
