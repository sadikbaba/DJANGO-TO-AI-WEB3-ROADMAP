from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm


def todo_list(request):

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo_list")

    # If it's just a normal page visit (GET request)
    else:
        form = TodoForm()

    tasks = Todo.objects.all()
    return render(request, "todo/todo_list.html", {"tasks": tasks, "form": form})


def complete_todo(request, pk):
    # Fetch the exact todo using its ID, or return a 404 page if it doesn't exist
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = True
    todo.save()  # What method do you call to save this change to the database?
    return redirect("todo_list")


def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()  # What method do you call to wipe this record from the database?
    return redirect("todo_list")
