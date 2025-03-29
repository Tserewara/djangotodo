from django.shortcuts import render

from todolist.models import Todo


def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todolist/todo_list.html', {'todos': todos})