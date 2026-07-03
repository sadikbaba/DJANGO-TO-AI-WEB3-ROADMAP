from django.shortcuts import render
from .models import Todo

# Create your views here.


def todo_list(request):
    tasks = Todo.objects.all()
    return render(request, "todo/todo_list.html", {"tasks": tasks})